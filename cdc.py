# This scripts compares Tnet and Phyloscanner on CDC detaset.
# Each outbreak is handeled separately in this script.
# We know the source of only 10 out of these outbreaks.

# Library Imports
from Bio import SeqIO
import operator
import shutil, os
import get_results as gr
import compare

# Global Variables
known_outbreaks = ['AA', 'AC', 'AI', 'AJ', 'AQ', 'AW', 'BA', 'BB', 'BC', 'BJ']

def get_cdc_true_transmission_edges():
	sources = ['AA45','AC124','AI004','AJ199','AQ89','AW2','BA3','BB45','BC46','BJ28']
	files = next(os.walk('CDC/fasta_files'))[2]
	files.sort()

	true_edges = []

	for source in sources:
		for file in files:
			if source[:2] == file[:2]:
				host = file.rstrip().split('_')[0]
				if source != host:
					true_edges.append(source +'->'+ host)

	return true_edges


def create_cdc_fasta_file():
	temp = []
	files = next(os.walk('CDC/all_fasta_files'))[2]
	files.sort()
	# print(len(files))

	records = []

	for file in files:
		if file[:2] in known_outbreaks:
			records.extend(list(SeqIO.parse('CDC/all_fasta_files/'+ file, 'fasta')))

	for i in range(len(records)):
	    # print(records[i].id)
	    parts = records[i].id.rstrip().split('_')
	    # print(parts[0] + '_N' + str(i))
	    records[i].id = parts[0] + '_N' + str(i)
	    records[i].name = ''
	    records[i].description = ''

	# print(len(records))

	for outbreak in known_outbreaks:
		temp = []
		for record in records:
			if record.id.startswith(outbreak):
				temp.append(record)
		# print(len(temp))
		os.mkdir("CDC/" + outbreak)
		SeqIO.write(temp, "CDC/" + outbreak + "/sequences.fasta", "fasta")

def create_raxml_output(bootstrap):
	for outbreak in known_outbreaks:
		input_file = os.path.abspath('CDC/'+ outbreak +'/sequences.fasta')
		output_folder = os.path.abspath('CDC/'+ outbreak +'/RAxML_output')

		cmd = 'raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s {} -w {} -N {} -n cdc -k'.format(input_file, output_folder, bootstrap)
		print(cmd)
		# os.system(cmd)

def create_cdc_phyloscanner_input():
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_input'
		output_folder = 'CDC/'+outbreak+'/phyloscanner_input'
		tree_list = next(os.walk(input_folder))[2]
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		for tree in tree_list:
			i = int(tree.rstrip().split('.')[1])
			rooted_tree = input_folder + '/' + tree
			rename_tree = output_folder + '/cdc_bootstrap.InWindow_'+ str(1000+i*100) +'_to_'+ str(1099+i*100) +'.tree'
			shutil.copy(rooted_tree, rename_tree)

def create_bootstrap_tree_files():
	for outbreak in known_outbreaks:
		bootstrap_trees_file = 'CDC/'+outbreak+'/RAxML_output/RAxML_bootstrap.cdc'
		output_folder = 'CDC/'+outbreak+'/RAxML_output/bootstrap_trees'
		f = open(bootstrap_trees_file)
		tree_list = f.readlines()
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		for i in range(len(tree_list)):
			file = open(output_folder + '/cdc.bootstrap.' + str(i), 'w')
			file.write(tree_list[i])

		# Add the RAxML_bestTree.cdc to the bootstrap tree files
		shutil.copy('CDC/'+outbreak+'/RAxML_output/RAxML_bestTree.cdc', output_folder + '/cdc.bootstrap.' + str(len(tree_list)))

def root_bootstrap_tree_files():
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/RAxML_output/bootstrap_trees'
		output_folder = 'CDC/'+outbreak+'/tnet_input'
		bootstrap_trees = next(os.walk(input_folder))[2]
		output_folder = os.path.abspath(output_folder)
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		for i in range(len(bootstrap_trees)):
			input_tree = input_folder + '/' + bootstrap_trees[i]
			cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(input_tree, i, output_folder)
			print(cmd)
			os.system(cmd)
			try:
				os.remove(output_folder + '/RAxML_info.' + str(i))
			except:
				print('RAxML_info does not exist')


def run_phyloscanner_cdc():
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/phyloscanner_input'
		output_folder = 'CDC/'+outbreak+'/phyloscanner_output'
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		input_file = input_folder + '/cdc_bootstrap.InWindow_'
		cmd = 'PhyloScanner/phyloscanner_analyse_trees.R {} cdc -ct -od {} s,0 --overwrite --tipRegex="^(.*)_(.*)$"'.format(input_file, output_folder)
		os.system(cmd)
		# print(cmd)


# Run tnet multiple times on single input_file tree and summery of all runs are listed in the output_file
# by default it will run 100 times
def run_tnet_multiple_times(input_file, output_file, time = 100):
	temp_out_file = output_file + '.temp'
	edge_dict = {}
	result = open(output_file, 'w+')

	for t in range(time):
		cmd = 'python3 TNet/tnet.py {} {}'.format(input_file, temp_out_file)
		os.system(cmd)
		e_list = []
		print(t,'Done')

		# Read result from temp_out_file and save to edge_dict
		f = open(temp_out_file)
		f.readline()
		for line in f.readlines():
			parts = line.split('\t')
			edge = parts[0]+'->'+parts[1]

			if edge not in e_list:
				if edge in edge_dict:
					edge_dict[edge] += 1
				else:
					edge_dict[edge] = 1
				e_list.append(edge)

		f.close()
		os.remove(temp_out_file)
		os.remove(input_file + '.temp')
		os.remove(input_file + '.tnet.log')
		# break

	edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))
	# print(edge_dict)

	for x, y in edge_dict.items():
		print(x, y)
		result.write('{}\t{}\n'.format(x, y))

	result.close()


def run_tnet_cdc():
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_input_renamed'
		output_folder = 'CDC/'+outbreak+'/tnet_output'
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)
		tree_list = next(os.walk(input_folder))[2]
		# print(tree_list)

		for tree in tree_list:
			input_file = input_folder +'/'+ tree
			output_file = output_folder +'/cdc_bootstrap.'+ tree.rstrip().split('.')[1]
			print(input_file, output_file)
			run_tnet_multiple_times(input_file, output_file)
			# break
		
		# break

def rename_outbreak_tnet_trees():
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_input'
		output_folder = 'CDC/'+outbreak+'/tnet_input_renamed'
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		for file in next(os.walk(input_folder))[2]:
			input_file = open(input_folder +'/'+ file)
			output_file = open(output_folder +'/'+ file, 'w+')
			line = input_file.readline()
			line = line.replace(outbreak,'')
			print(line)
			output_file.write(line)
			input_file.close()
			output_file.close()


def rename_tnet_trees(input_folder, output_folder):
	mapping = {}
	f = open('CDC/file_to_ID_mapping.csv')
	for line in f.readlines():
		parts = line.rstrip().split(',')
		name = parts[1].split('_')[0]
		# print(name)
		mapping[name] = parts[0]

	f.close()
	# print(mapping)
	tree_list = next(os.walk(input_folder))[2]
	for tree in tree_list:
		print('Tree file: ' + tree)
		input_file = open(input_folder +'/'+ tree)
		output_file = open(output_folder +'/'+ tree, 'w+')
		line = input_file.readline()

		for x, y in mapping.items():
			line = line.replace(x,y)

		print(line)
		output_file.write(line)
		input_file.close()
		output_file.close()
		# break




def main():
	# create_cdc_fasta_file()
	# create_raxml_output(20)
	# create_bootstrap_tree_files()
	# root_bootstrap_tree_files()
	# create_cdc_phyloscanner_input()
	# run_phyloscanner_cdc()
	# run_tnet_cdc('CDC/tnet_input_renamed','CDC/tnet_output',50)
	# rename_outbreak_tnet_trees()
	run_tnet_cdc()


	# print(get_cdc_true_transmission_edges())
	# phylo_multi_with_complex = set(gr.get_phyloscanner_multi_tree_edges_with_complex('CDC/phyloscanner_output_known/CDC_hostRelationshipSummary.csv', 11))
	# real = set(get_cdc_true_transmission_edges())

	# TP = len(compare.intersection(real, phylo_multi_with_complex))
	# FP = len(compare.minus(phylo_multi_with_complex,real))
	# FN = len(compare.minus(real,phylo_multi_with_complex))

	# print(TP, FP,FN)

	


if __name__ == "__main__": main()
