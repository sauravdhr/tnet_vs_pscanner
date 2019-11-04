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
sources = ['AA45','AC124','AI4','AJ199','AQ89','AW2','BA3','BB45','BC46','BJ28']

def get_true_transmission_edges(outbreak):
	seq_list = list(SeqIO.parse('CDC/'+ outbreak +'/sequences.fasta', 'fasta'))

	true_edges = []
	hosts = []
	for seq in seq_list:
		hosts.append(seq.id.split('_')[0])

	hosts = list(set(hosts))
	# print(hosts)

	for source in sources:
		if source.startswith(outbreak):
			s = source.replace(outbreak, '')
			for host in hosts:
				if s != host:
					true_edges.append(s +'->'+ host)

	return true_edges


def create_cdc_fasta_file():
	files = next(os.walk('CDC/all_fasta_files'))[2]
	files.sort()

	records = {}

	for outbreak in known_outbreaks:
		temp = []
		for file in files:
			if file.startswith(outbreak):
				temp.extend(list(SeqIO.parse('CDC/all_fasta_files/'+ file, 'fasta')))

		records[outbreak] = temp

	for outbreak, record_list in records.items():
		for i in range(len(record_list)):
			parts = record_list[i].id.split('_')
			host = int(parts[0][2:])
			record_list[i].id = str(host) + '_N' + str(i)

		os.mkdir("CDC/" + outbreak)
		SeqIO.write(record_list, "CDC/" + outbreak + "/sequences.fasta", "fasta")


	# for file in files:
	# 	if file[:2] in known_outbreaks:
	# 		records.extend(list(SeqIO.parse('CDC/all_fasta_files/'+ file, 'fasta')))

	# for i in range(len(records)):
	#     # print(records[i].id)
	#     parts = records[i].id.rstrip().split('_')
	#     # print(parts[0] + '_N' + str(i))
	#     records[i].id = parts[0] + '_N' + str(i)
	#     records[i].name = ''
	#     records[i].description = ''

	# # print(len(records))

	# for outbreak in known_outbreaks:
	# 	temp = []
	# 	for record in records:
	# 		if record.id.startswith(outbreak):
	# 			temp.append(record)
	# 	# print(len(temp))
	# 	os.mkdir("CDC/" + outbreak)
	# 	SeqIO.write(temp, "CDC/" + outbreak + "/sequences.fasta", "fasta")



def create_raxml_output(bootstrap):
	for outbreak in known_outbreaks:
		input_file = os.path.abspath('CDC/'+ outbreak +'/sequences.fasta')
		output_folder = os.path.abspath('CDC/'+ outbreak +'/RAxML_output')
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		cmd = 'raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s {} -w {} -N {} -n cdc -k'.format(input_file, output_folder, bootstrap)
		# print(cmd)
		os.system(cmd)
		try:
			os.remove(output_folder + '/RAxML_info.cdc')
		except:
			print('RAxML_info does not exist')

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
		input_folder = 'CDC/'+ outbreak +'/RAxML_output/bootstrap_trees'
		output_folder = 'CDC/'+ outbreak +'/tnet_input'
		bootstrap_trees = next(os.walk(input_folder))[2]
		output_folder = os.path.abspath(output_folder)
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)

		for tree in bootstrap_trees:
			input_tree = input_folder + '/' + tree
			i = int(tree.split('.')[2])
			cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(input_tree, str(i), output_folder)
			# print(cmd)
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
		# f.readline()
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


# Run tnet multiple times on single input_file tree and summery of all runs are listed in the output_file
# by default it will run 100 times and directed and undirected counts are made
def run_tnet_multiple_times_both_directed_undirected(input_file, output_file, undirected_output_file, time = 100):
	temp_out_file = output_file + '.temp'
	edge_dict = {}
	undirected_edge_dict = {}

	for t in range(time):
		cmd = 'python3 TNet/tnet.py {} {}'.format(input_file, temp_out_file)
		os.system(cmd)
		e_list = []
		un_e_list = []
		print(t,'Done')

		# Read result from temp_out_file and save to edge_dict
		f = open(temp_out_file)
		# f.readline()
		for line in f.readlines():
			parts = line.split('\t')
			edge = parts[0]+'->'+parts[1]
			rev_edge = parts[1]+'->'+parts[0]
			# print(edge, rev_edge)

			if edge not in e_list:
				if edge in edge_dict:
					edge_dict[edge] += 1
				else:
					edge_dict[edge] = 1
				e_list.append(edge)

			if edge not in un_e_list and rev_edge not in un_e_list:
				# print(len(un_e_list), un_e_list)
				if edge in undirected_edge_dict:
					undirected_edge_dict[edge] += 1
				elif rev_edge in undirected_edge_dict:
					undirected_edge_dict[rev_edge] += 1
				else:
					undirected_edge_dict[edge] = 1
				un_e_list.append(edge)

		f.close()
		os.remove(temp_out_file)
		os.remove(input_file + '.temp')
		os.remove(input_file + '.tnet.log')
		# break

	edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))
	print(len(edge_dict), edge_dict)
	undirected_edge_dict = dict(sorted(undirected_edge_dict.items(), key=operator.itemgetter(1),reverse=True))
	print(len(undirected_edge_dict), undirected_edge_dict)

	result = open(output_file, 'w+')
	for x, y in edge_dict.items():
		result.write('{}\t{}\n'.format(x, y))

	result.close()

	result = open(undirected_output_file, 'w+')
	for x, y in undirected_edge_dict.items():
		result.write('{}\t{}\n'.format(x, y))

	result.close()

def run_tnet_cdc():
	# known_outbreaks = ['AW']
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_input'
		output_folder = 'CDC/'+outbreak+'/tnet_output'
		undirected_output_folder = 'CDC/'+outbreak+'/tnet_output_undirected'
		if not os.path.exists(output_folder):
			os.mkdir(output_folder)
		if not os.path.exists(undirected_output_folder):
			os.mkdir(undirected_output_folder)
		tree_list = next(os.walk(input_folder))[2]

		for tree in tree_list:
			input_file = input_folder +'/'+ tree
			output_file = output_folder +'/cdc_bootstrap.'+ tree.rstrip().split('.')[1]
			undirected_output_file = undirected_output_folder +'/cdc_bootstrap.'+ tree.rstrip().split('.')[1]
			if not os.path.exists(output_file):
				# run_tnet_multiple_times(input_file, output_file)
				run_tnet_multiple_times_both_directed_undirected(input_file, output_file, undirected_output_file)
			# break
		# break


def create_cdc_tnet_summary(th=50):
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_output'
		output_folder = 'CDC/'+outbreak
		edge_dict = {}
		result = open(output_folder+'/tnet.summary.'+ str(th), 'w+')

		tnet_list = next(os.walk(input_folder))[2]
		for tnet in tnet_list:
			input_file = input_folder+'/'+ tnet
			f = open(input_file)
			for line in f.readlines():
				parts = line.rstrip().split('\t')
				edge = parts[0]
				# print(parts)
				if int(parts[1]) < th: continue
				if edge in edge_dict:
					edge_dict[edge] += 1
				else:
					edge_dict[edge] = 1

			f.close()

		edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))

		for x, y in edge_dict.items():
			result.write('{}\t{}\n'.format(x, y))

		result.close()

def create_cdc_tnet_summary_undirected(th=50):
	for outbreak in known_outbreaks:
		input_folder = 'CDC/'+outbreak+'/tnet_output_undirected'
		output_folder = 'CDC/'+outbreak
		edge_dict = {}
		result = open(output_folder+'/tnet.summary.undirected.'+ str(th), 'w+')

		tnet_list = next(os.walk(input_folder))[2]
		for tnet in tnet_list:
			input_file = input_folder+'/'+ tnet
			f = open(input_file)
			for line in f.readlines():
				parts = line.rstrip().split('\t')
				edge = parts[0]
				# print(parts)
				if int(parts[1]) < th: continue
				if edge in edge_dict:
					edge_dict[edge] += 1
				else:
					edge_dict[edge] = 1

			f.close()

		edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))

		for x, y in edge_dict.items():
			result.write('{}\t{}\n'.format(x, y))

		result.close()


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

def compare_cdc_directed(th=50):
	TP_FP_FN_file = open('CDC/cdc.directed.80.th_' +str(th)+ '.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('outbreak,phylo_tp,phylo_fp,phylo_fn,tnet_tp,tnet_fp,tnet_fn\n')
	F1_file = open('CDC/cdc.directed.80.th_' +str(th)+ '.F1.csv', 'w+')
	F1_file.write('outbreak,phylo_prec,phylo_rec,phylo_f1,tnet_prec,tnet_rec,tnet_f1\n')

	for outbreak in known_outbreaks:
		print('outbreak: ', outbreak)

		TP_FP_FN = []
		F1 = []

		real = set(get_true_transmission_edges(outbreak))
		phylo = set(gr.get_phyloscanner_multi_tree_edges_with_complex('CDC/'+ outbreak +'/phyloscanner_output/cdc_hostRelationshipSummary.csv', 21))
		tnet = set(gr.get_summary_tnet_edges('CDC/'+ outbreak +'/tnet.summary.80', 21))
		print(real)
		print(phylo)
		print(tnet)
		

		TP = len(real & phylo)
		FP = len(phylo - real)
		FN = len(real - phylo)
		try:
			precision = TP/(TP+FP)
			recall = TP/(TP+FN)
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			precision = 0
			recall = 0
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		TP = len(real & tnet)
		FP = len(tnet - real)
		FN = len(real - tnet)
		try:
			precision = TP/(TP+FP)
			recall = TP/(TP+FN)
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			precision = 0
			recall = 0
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		print(TP_FP_FN)
		print(F1)
		TP_FP_FN_file.write('{},{},{},{},{},{},{}\n'.format(outbreak,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5]))
		F1_file.write('{},{},{},{},{},{},{}\n'.format(outbreak,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5]))
		# break


def compare_cdc_undirected(th=50):
	TP_FP_FN_file = open('CDC/undirected.cdc.80.th_'+ str(th) +'.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('outbreak,phylo_tp,phylo_fp,phylo_fn,tnet_tp,tnet_fp,tnet_fn\n')
	F1_file = open('CDC/undirected.cdc.80.th_'+ str(th) +'.F1.csv', 'w+')
	F1_file.write('outbreak,phylo_prec,phylo_rec,phylo_f1,tnet_prec,tnet_rec,tnet_f1\n')

	for outbreak in known_outbreaks:
		print('outbreak: ', outbreak)

		TP_FP_FN = []
		F1 = []

		real = set(get_true_transmission_edges(outbreak))
		phylo = set(gr.get_phyloscanner_multi_tree_edges_with_complex('CDC/'+ outbreak +'/phyloscanner_output/cdc_hostRelationshipSummary.csv', 13))
		tnet = set(get_undirected_tnet_summary('CDC/'+ outbreak +'/tnet.summary.undirected.80', 13))
		print(real)
		print(phylo)
		print(tnet)
		

		TP = len(compare.intersection(real, phylo))
		FP = len(compare.minus(phylo,real))
		FN = len(compare.minus(real,phylo))
		try:
			precision = TP/(TP+FP)
			recall = TP/(TP+FN)
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			precision = 0
			recall = 0
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		TP = len(compare.intersection(real, tnet))
		FP = len(compare.minus(tnet,real))
		FN = len(compare.minus(real,tnet))
		try:
			precision = TP/(TP+FP)
			recall = TP/(TP+FN)
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			precision = 0
			recall = 0
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		print(TP_FP_FN)
		print(F1)
		TP_FP_FN_file.write('{},{},{},{},{},{},{}\n'.format(outbreak,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5]))
		F1_file.write('{},{},{},{},{},{},{}\n'.format(outbreak,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5]))
		# break


def get_undirected_tnet_summary(file, cutoff):
	edges = []
	edge_dict = {}
	f = open(file)

	for line in f.readlines():
		if line.startswith('None'): continue
		parts = line.rstrip().split('\t')
		edge = parts[0]
		e_parts = edge.split('->')
		rev_edge = e_parts[1]+'->'+e_parts[0]

		if edge in edge_dict:
			edge_dict[edge] += int(parts[1])
		elif rev_edge in edge_dict:
			edge_dict[rev_edge] += int(parts[1])
		else:
			edge_dict[edge] = int(parts[1])

	f.close()
	for x, y in edge_dict.items():
		print(x, y)
		if y > cutoff: edges.append(x)

	return edges



def main():
	# create_cdc_fasta_file()
	# create_raxml_output(25)
	# create_bootstrap_tree_files()
	# root_bootstrap_tree_files()
	# create_cdc_phyloscanner_input()
	# run_phyloscanner_cdc()
	# run_tnet_cdc('CDC/tnet_input_renamed','CDC/tnet_output',50)
	# rename_outbreak_tnet_trees()
	# run_tnet_cdc()
	# create_cdc_tnet_summary(80)
	# create_cdc_tnet_summary_undirected(80)



	# compare_cdc_directed(80)
	compare_cdc_undirected(50)
	# phylo_multi_with_complex = set(gr.get_phyloscanner_multi_tree_edges_with_complex('CDC/phyloscanner_output_known/CDC_hostRelationshipSummary.csv', 11))
	# real = set(get_cdc_true_transmission_edges())

	# TP = len(compare.intersection(real, phylo_multi_with_complex))
	# FP = len(compare.minus(phylo_multi_with_complex,real))
	# FN = len(compare.minus(real,phylo_multi_with_complex))

	# print(TP, FP,FN)

	


if __name__ == "__main__": main()
