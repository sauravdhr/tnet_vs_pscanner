import os
import json
# import dendropy
# from dendropy.interop import seqgen
import threading

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

def multithreadings(input_file, i, output_dir):
	os.mkdir(output_dir)
	cmd = 'raxmlHPC -f a -x 12345 -p 12345 -s {} -n {} -w {} -m GTRGAMMA -N 25'.format(input_file, i, output_dir) 
	# print(cmd)
	os.system(cmd)
	os.remove(output_dir + '/RAxML_info.' + str(i))
	   
def create_raxml_trees(folder, num):
	t=[]
	for i in range(num):
		input_file = 'seqgen/' +folder+ '/seqgen.seqs.' + str(i)
		output_dir = '/home/saurav/Dropbox/Research/tnet_vs_pscanner/seqgen/' +folder+ '/RAxML_' + str(i)
		if os.path.exists(output_dir):
			print('Already exists')
		else:
			t[i] = threading.Thread(target=multithreadings, args=(input_file, i, output_dir))
			t[i].start()
			# Rooting the best RAxML tree
			best_tree = output_dir + '/RAxML_bestTree.' + str(i)
			cmd = 'raxmlHPC -f I -m GTRGAMMA -t {} -n {} -w {}'.format(best_tree, i, output_dir)
			os.system(cmd)

	for i in range(num):
		t[i].join()


def main():
	root_dir = '/home/saurav/research/Favites_data_from_sam/'

	print('Please choose one of the following datasets->')
	print(next(os.walk(root_dir))[1])

	dataset = 'SEIR01'
	print('You choose->',dataset)

	data_dir = root_dir + dataset
	folders = next(os.walk(data_dir))[1]
	folders = folders[:2]

	for folder in folders:
		print('inside folder: ',folder)
		# create_seqgen_file(folder)
		# create_seqgen_sequences(folder,10)
		create_raxml_trees(folder, 10)

		# cur_dir = 'outputs/' + folder + '/'
		# break





if __name__ == "__main__": main()