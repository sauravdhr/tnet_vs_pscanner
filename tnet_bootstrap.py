import os
import json
# import dendropy
# from dendropy.interop import seqgen
import threading
import get_results as gr

# #############
# truetree = dendropy.TreeList.get(path="true.tree", schema="newick")
# # congif seq-gen
# s = seqgen.SeqGen()
# s.char_model = seqgen.SeqGen.GTR


# t0 = s.generate(truetree)
# print(t0.char_matrices[0].as_string("fasta"))
# #############


# cmd = 'seq-gen -m GTR -a 0.1 -of < true.tree > seq.root.fasta'
# os.system(cmd)

# hosts = {}

# f = open('seq.fasta')
# for line in f.readlines():
# 	if line[0]=='>':
# 		# print(line)
# 		parts = line.rstrip().split('_')
# 		if parts[0] in hosts:
# 			hosts[parts[0]] += 1
# 		else:
# 			hosts[parts[0]] = 1

# print(hosts)
# print(len(hosts))


def create_seqgen_file(folder):
	parts = folder.split('_')

	# get the source seq from json config file
	json_file = '/home/saurav/research/Favites_data_from_sam/' + parts[0] + '/' + folder + '/' + folder + '.config'
	# print(json_file)
	data = json.load(open(json_file))
	root_seq = data["seed_seqs"][0]
	# print(root_seq)

	# get the true tree from the true.tree file
	tree_file = '/home/saurav/research/Favites_data_from_sam/' + parts[0] + '/' + folder + '/clean_data/'+ folder +'.true.tree'
	f = open(tree_file)
	true_tree = f.readline()

	# Write the Seq-Gen input file
	if os.path.exists('seqgen/' + folder):
		print('Already exists')
	else:
		os.mkdir('seqgen/' + folder)
		seqgen_file = open('seqgen/' + folder + '/seqgen.input', 'w+')
		seqgen_file.write('{} {}\n'.format(1, len(root_seq)))
		seqgen_file.write('{} {}\n'.format('N1', root_seq))
		seqgen_file.write('{}\n'.format(1))
		seqgen_file.write('{}'.format(true_tree))

	
def create_seqgen_sequences(folder, num):
	input_file = 'seqgen/' +folder+ '/seqgen.input'
	# output_file = 'seqgen/' +folder+ '/seqgen.seqs'
	# get parameters from json config file
	parts = folder.split('_')
	json_file = '/home/saurav/research/Favites_data_from_sam/' + parts[0] + '/' + folder + '/' + folder + '.config'
	data = json.load(open(json_file))

	# run Seq-Gen
	gamma_shape = data["seqgen_gamma_shape"]
	rate_matrix = data["seqgen_a_to_c"],data["seqgen_a_to_g"],data["seqgen_a_to_t"],data["seqgen_c_to_g"],data["seqgen_c_to_t"],data["seqgen_g_to_t"]
	rate_matrix = str(rate_matrix)
	rate_matrix = rate_matrix.replace('(','').replace(')','')
	print(rate_matrix)
	frequencies = data["seqgen_freq_a"],data["seqgen_freq_c"],data["seqgen_freq_g"],data["seqgen_freq_t"]
	frequencies = str(frequencies)
	frequencies = frequencies.replace('(','').replace(')','')
	print(frequencies)

	for i in range(num):
		output_file = 'seqgen/' +folder+ '/seqgen.seqs.' + str(i)
		cmd = 'seq-gen -m GTR -a {} -r {} -f {} -of < {} > {}'.format(gamma_shape,rate_matrix,frequencies,input_file,output_file)
		print(cmd)
		os.system(cmd)


def create_raxml_trees(folder, num):
	for i in range(num):
		input_file = 'seqgen/' +folder+ '/seqgen.seqs.' + str(i)
		output_dir = '/home/saurav/Dropbox/Research/tnet_vs_pscanner/seqgen/' +folder+ '/RAxML_' + str(i)
		if os.path.exists(output_dir):
			print('Already exists')
		else:
			os.mkdir(output_dir)
			# cmd = 'raxmlHPC -f a -x 12345 -p 12345 -s {} -n {} -w {} -m GTRGAMMA -N 25'.format(input_file, i, output_dir)
			# print(cmd)
			# os.system(cmd)
			# os.remove(output_dir + '/RAxML_info.' + str(i))

			# # Rooting the best RAxML tree
			# best_tree = output_dir + '/RAxML_bestTree.' + str(i)
			# cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(best_tree, i, output_dir)
			# os.system(cmd)

def root_raxml_best_trees(n):
	cur_dir = '/home/saurav/Dropbox/Research/tnet_vs_pscanner/seqgen/'
	folders = next(os.walk(cur_dir))[1]

	# print(folders)
	print('total',len(folders))
	for folder in folders:
		print('inside folder: ',folder)
		for i in range(n):
			output_dir = cur_dir + folder + '/RAxML_' + str(i)
			best_tree = output_dir + '/RAxML_bestTree.' + str(i)
			rooted_tree = output_dir + '/RAxML_rootedTree.' + str(i)
			info = output_dir + '/RAxML_info.' + str(i)

			if os.path.exists(rooted_tree):
				print('Already rooted')
			else:
				if os.path.exists(best_tree):
					cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(best_tree, i, output_dir)
					print(cmd)
					os.system(cmd)
					try:
						os.remove(output_dir + '/RAxML_info.' + str(i))
					except:
						print('cool')
				else:
					print('Best tree does not exist')


def create_bash_scripts(num):
	cmd_list = []
	folders = next(os.walk('seqgen/'))[1]
	for folder in folders:
		for i in range(num):
			best_tree = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_bestTree.' + str(i)
			info = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_info.' + str(i)
			if os.path.exists(best_tree): continue
			if os.path.exists(info):
				input_file = 'seqgen/' +folder+ '/seqgen.seqs.' + str(i)
				output_dir = '/data/saurav/seqgen/' +folder+ '/RAxML_' + str(i)

				cmd = 'raxmlHPC -f a -x 12345 -p 12345 -s {} -n {} -w {} -m GTRGAMMA -N 25'.format(input_file, i, output_dir)
				print(cmd)
				cmd_list.append(cmd)

	print(len(cmd_list))

	# for i in range(len(cmd_list)):
	# 	print(i%60, cmd_list[i])
	# 	script = open('raxml_scripts/' + str(i%60) + '.raxml_cmd.sh', 'a+')
	# 	script.write(cmd_list[i] + '\n')
	# 	script.close()

def run_script(folder, script):
	cmd = './'+folder+script
	print(cmd)
	os.system(cmd)

def raxml_scripts_threaded(folder):
	t=[]
	scripts = next(os.walk(folder))[2]
	# print(scripts)
	for script in scripts:
		print(folder+script)
		t.append(threading.Thread(target=run_script, args=(folder, script)))
		# run_script(folder+script)

	for i in range(len(t)):
		t[i].start()

	for i in range(len(t)):
		t[i].join()

def check_and_clean_seqgen(num):
	info_count = 0
	best_count = 0
	rooted_count = 0
	phylo_trees_count = 0
	cur_dir = '/home/saurav/Dropbox/Research/tnet_vs_pscanner/seqgen/'
	# cur_dir = '/home/saurav/research/seqgen_server/'
	folders = next(os.walk(cur_dir))[1]
	print('Total set:',len(folders))

	for folder in folders:
		phylo_trees = cur_dir+folder+'/phylo_trees'
		if os.path.exists(phylo_trees):
			phylo_trees_count += 1
			# gr.create_phylo_multi_tree_input(folder)

		for i in range(num):
			best_tree = cur_dir+folder+'/RAxML_'+ str(i)+'/RAxML_bestTree.' + str(i)
			info_file = cur_dir+folder+'/RAxML_'+ str(i)+'/RAxML_info.' + str(i)
			rooted_tree = cur_dir+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)

			if os.path.exists(rooted_tree): rooted_count += 1
			if os.path.exists(best_tree):
				best_count += 1
				# print(folder, i)
			if os.path.exists(info_file):
				info_count += 1
				# os.remove(info_file)
				print(folder, i)


	print('Total :',len(folders)*10)
	print('Best :' +str(best_count)+ ' Info :' +str(info_count)+ ' Rooted :'+str(rooted_count))
	print('Phylo_trees :' +str(phylo_trees_count))

def main():
	# root_dir = '/home/saurav/research/Favites_data_from_sam/'

	# print('Please choose one of the following datasets->')
	# print(next(os.walk(root_dir))[1])

	# dataset = 'SIR003'
	# dataset_list = ['SEIR015','SIR01','SIR003']
	# print('You choose->',dataset)

	# data_dir = root_dir + dataset
	# folders = next(os.walk(data_dir))[1]
	# print('total',len(folders))
	# folders = folders[:2]

	# for folder in folders:
		# print('inside folder: ',folder)
		# create_seqgen_file(folder)
		# create_seqgen_sequences(folder,10)
		# create_raxml_trees(folder, 10)

		# cur_dir = 'result/' + folder + '/'
		# break
	# print('DONE')

	# for i in range(0,len(folders),6):
	# 	points = folders[i:i+6]
	# 	print(i,points)
	# 	print('DONE UPTO',i+len(points))


	check_and_clean_seqgen(10)
	# root_raxml_best_trees(10)
	# create_bash_scripts(10)
	# raxml_scripts_threaded('raxml_scripts/')


if __name__ == "__main__": main()