from Bio import SeqIO
import operator
import shutil, os

def get_true_transmission_edges():
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
	files = next(os.walk('CDC/fasta_files'))[2]
	files.sort()
	print(len(files))

	known_outbreaks = ['AA', 'AC', 'AI', 'AJ', 'AQ', 'AW', 'BA', 'BB', 'BC', 'BJ']
	# mapping = open('CDC/file_to_ID_mapping.csv', 'w+')

	records = []
	# id_count = 1

	for file in files:
		if file[:2] in known_outbreaks:
			records.extend(list(SeqIO.parse('CDC/fasta_files/'+ file, 'fasta')))
		# mapping.write('{},{}\n'.format(id_count, file))
		# id_count += 1

	# mapping.close()

	# print(len(records))
	for i in range(len(records)):
	    # print(records[i].id)
	    parts = records[i].id.rstrip().split('_')
	    # print(parts[0] + '_N' + str(i))
	    records[i].id = parts[0] + '_N' + str(i)
	    records[i].name = ''
	    records[i].description = ''

	# # print(records)
	# SeqIO.write(records, "CDC/AA_to_BX.fasta", "fasta")
	SeqIO.write(records, "CDC/known_outbreaks.fasta", "fasta")


def create_raxml_output(input_file, output_folder, bootstrap):
	input_file = '/home/saurav/research/tnet_vs_pscanner/' + input_file
	output_folder = '/home/saurav/research/tnet_vs_pscanner/' + output_folder
	cmd = 'raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s {} -w {} -N {} -n cdc -k'.format(input_file, output_folder, bootstrap)
	print(cmd)
	# os.system(cmd)

def create_cdc_phyloscanner_input(input_folder, output_folder):
	tree_list = next(os.walk(input_folder))[2]

	for tree in tree_list:
		i = int(tree.rstrip().split('.')[1])
		# print(i)
		rooted_tree = input_folder + '/' + tree
		rename_tree = output_folder + '/CDC_bootstrap.InWindow_'+ str(1000+i*100) +'_to_'+ str(1099+i*100) +'.tree'
		# print(rooted_tree, rename_tree)
		shutil.copy(rooted_tree, rename_tree)

def create_bootstrap_tree_files(bootstrap_trees_file, output_folder):
	f = open(bootstrap_trees_file)
	tree_list = f.readlines()
	if not os.path.exists(output_folder):
		os.mkdir(output_folder)
	
	for i in range(len(tree_list)):
		file = open(output_folder + '/cdc.bootstrap.' + str(i), 'w')
		file.write(tree_list[i])

	# Add the RAxML_bestTree.cdc to the bootstrap tree files
	shutil.copy('CDC/RAxML_output/RAxML_bestTree.cdc', output_folder + '/cdc.bootstrap.' + str(len(tree_list)))

def root_bootstrap_tree_files(input_folder, output_folder):
	tree_list = next(os.walk(input_folder))[2]

	for i in range(len(tree_list)):
		input_tree = input_folder + '/' + tree_list[i]
		cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(input_tree, i, output_folder)
		print(cmd)
		os.system(cmd)
		try:
			os.remove(output_folder + '/RAxML_info.' + str(i))
		except:
			print('cool')


def run_phyloscanner_cdc(input_folder, output_folder):
	input_file = input_folder + '/CDC_bootstrap.InWindow_'
	cmd = 'PhyloScanner/phyloscanner_analyse_trees.R {} CDC -ct -od {} s,0 --overwrite --tipRegex="^(.*)_(.*)$"'.format(input_file, output_folder)
	# os.system(cmd)
	print(cmd)


# Run tnet multiple times on single input_file tree and summery of all runs are listed in the output_file
# by default it will run 100 times
def run_tnet_multiple_times(input_file, output_file, time = 100):
	temp_out_file = output_file + '.out'
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


def run_tnet_cdc(input_folder, output_folder, th):
	# tree_list = next(os.walk(input_folder))[2]
	tree_list = ['RAxML_rootedTree.8']
	print(tree_list)

	for tree in tree_list:
		input_file = input_folder +'/'+ tree
		output_file = output_folder +'/CDC_bootstrap.'+ tree.rstrip().split('.')[1]
		# print(input_file, output_file)
		run_tnet_multiple_times(input_file, output_file)
		# break


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
		break




def main():
	# create_cdc_fasta_file()
	# create_raxml_output('CDC/known_outbreaks.fasta', 'CDC/RAxML_output_known', 20)
	# create_bootstrap_tree_files('CDC/RAxML_output_known/RAxML_bootstrap.cdc','CDC/RAxML_output_known/bootstrap_trees')
	# root_bootstrap_tree_files('CDC/RAxML_output_known/bootstrap_trees','/home/saurav/research/tnet_vs_pscanner/CDC/tnet_input_known')
	# create_cdc_phyloscanner_input('CDC/tnet_input_known','CDC/phyloscanner_input_known')
	# run_phyloscanner_cdc('CDC/phyloscanner_input_known','CDC/phyloscanner_output_known')
	# run_tnet_cdc('CDC/tnet_input_known','CDC/tnet_output_known',50)
	# rename_tnet_trees('CDC/tnet_input', 'CDC/tnet_input_renamed')


	print(get_true_transmission_edges())

	


if __name__ == "__main__": main()
