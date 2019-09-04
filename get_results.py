import shutil, os
import operator

def tnet_multiple(input_file, output_file, time):
	out_file = output_file + '.out'
	edge_dict = {}
	result = open(output_file + '.multiple', 'w+')

	for t in range(time):
		cmd = 'python3 TNet/tnet.py {} {}'.format(input_file, out_file)
		os.system(cmd)
		e_list = []
		# print(t,'Done')

		f = open(out_file)
		f.readline()
		for line in f.readlines():
			# print('Line : ', line)
			parts = line.split('\t')
			edge = parts[0]+'->'+parts[1]

			if edge not in e_list:
				if edge in edge_dict:
					edge_dict[edge] += 1
				else:
					edge_dict[edge] = 1
				e_list.append(edge)

		f.close()
		os.remove(out_file)
		os.remove(input_file + '.temp')
		os.remove(input_file + '.tnet.log')
		# break

	# edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))
	# print(edge_dict)

	for x, y in edge_dict.items():
		# print(x, y)
		result.write('{}\t{}\n'.format(x, y))

	result.close()

def phyloscanner_multi_tree(folder):
	phylo_trees_dir = 'seqgen/'+folder+'/phylo_trees'
	result_dir = 'result/'+folder+'/phyloscanner_multi_tree'
	if os.path.exists(result_dir): return True
	if not os.path.exists(phylo_trees_dir): return False

	os.mkdir(result_dir)
	input_file = phylo_trees_dir + '/RAxML_rootedTree.InWindow_'
	cmd = 'PhyloScanner/phyloscanner_analyse_trees.R {} seqgen -ct -od {} s,0 --overwrite --tipRegex="^(.*)_(.*)$"'.format(input_file, result_dir)
	os.system(cmd)
	# print(cmd)

	files = os.listdir(result_dir)
	for file in files:
		if 'processedTree' in file:
			# print(file)
			os.remove(os.path.join(result_dir,file))

	return True

def all_rooted_trees_exist(folder):
	for i in range(10):
		rooted_tree = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)
		if not os.path.exists(rooted_tree):
			return False
		
	return True

def create_phylo_multi_tree_input(folder):
	phylo_trees_dir = 'seqgen/'+folder+'/phylo_trees'
	if os.path.exists(phylo_trees_dir): return True
	if not all_rooted_trees_exist(folder): return False
	
	os.mkdir(phylo_trees_dir)
	for i in range(10):
		rooted_tree = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)
		rename_tree = phylo_trees_dir + '/RAxML_rootedTree.InWindow_'+ str(1000+i*100) +'_to_'+ str(1099+i*100) +'.tree'
		shutil.copy(rooted_tree, rename_tree)

	return True

def generate_outputs(data_dir, folders):
	# Generating outputs
	for folder in folders:
		print('Now in folder->',folder)
		cur_dir = data_dir + '/' + folder + '/clean_data/'
		# print('Files here->',next(os.walk(cur_dir))[2])

		# Create results directory
		out_dir = 'result/' + folder
		# os.mkdir(out_dir)

		# Running TNet on the RAxML tree
		input_file = cur_dir + folder + '.raxml'
		output_file = out_dir + '/raxml.tree.tnet'
		cmd = 'python3 TNet/tnet.py {} {}'.format(input_file, output_file)
		os.system(cmd)
		os.remove(input_file + '.temp')
		os.remove(input_file + '.tnet.log')
		os.remove(output_file + '.multiple')
		# TNet with multiple sampling
		# tnet_multiple(input_file, output_file, 100)


		# Running TNet on the true tree
		input_file = cur_dir + folder + '.true.tree'
		output_file = out_dir + '/true.tree.tnet'
		os.remove(output_file)
		cmd = 'python3 TNet/tnet.py {} {}'.format(input_file, output_file)
		os.system(cmd)
		os.remove(input_file + '.temp')
		os.remove(input_file + '.tnet.log')
		# TNet with multiple sampling
		# tnet_multiple(input_file, output_file, 100)

		# Running PhyloScanner on the RAxML tree
		phy_dir = out_dir + '/phyloscanner'
		os.mkdir(phy_dir)
		input_file = cur_dir + folder + '.raxml'
		output_file = 'raxml.tree'
		cmd = 'PhyloScanner/phyloscanner_analyse_trees.R {} {} -cd -ct -od {} s,0 --overwrite --tipRegex="^(.*)_(.*)$"'.format(input_file, output_file, phy_dir)
		os.system(cmd)

		# Running PhyloScanner on the true tree
		input_file = cur_dir + folder + '.true.tree'
		output_file = 'true.tree'
		cmd = 'PhyloScanner/phyloscanner_analyse_trees.R {} {} -cd -ct -od {} s,0 --overwrite --tipRegex="^(.*)_(.*)$"'.format(input_file, output_file, phy_dir)
		os.system(cmd)
		# break

	print('OUTPUT GENERATION FINISHED')


def get_real_edges(real_file):
	real_edges = []
	f = open(real_file)
	f.readline()
	for line in f.readlines():
		parts = line.split('\t')
		if not parts[0] == parts[1]:
			real_edges.append(parts[0]+'->'+parts[1])
		# print(parts)

	f.close()
	return real_edges


def get_phyloscanner_edges(phylo_file):
	phyloscanner_edges = []
	f = open(phylo_file)
	f.readline()
	for line in f.readlines():
		parts = line.rstrip().split(',')
		if parts[2].isdigit() and parts[3].isdigit():
			phyloscanner_edges.append(parts[3]+'->'+parts[2])
		# print(parts)

	f.close()
	return phyloscanner_edges

def get_phyloscanner_multi_tree_edges(phylo_file, cutoff):
	phyloscanner_edges = []
	f = open(phylo_file)
	f.readline()
	for line in f.readlines():
		parts = line.rstrip().split(',')
		# print(parts)
		if parts[2] == 'trans' and int(parts[3]) > cutoff:
			phyloscanner_edges.append(parts[0]+'->'+parts[1])
		# print(parts)

	f.close()
	return phyloscanner_edges


def get_phyloscanner_multi_tree_edges_with_complex(phylo_file, cutoff):
	phyloscanner_edges = []
	edge_dict = {}
	f = open(phylo_file)
	f.readline()
	for line in f.readlines():
		parts = line.rstrip().split(',')
		# print(parts)
		if parts[2] == 'trans' or parts[2] == 'complex':
			edge = parts[0]+'->'+parts[1]
			if edge in edge_dict:
				edge_dict[edge] += int(parts[3])
			else:
				edge_dict[edge] = int(parts[3])
		# print(parts)

	f.close()
	for x, y in edge_dict.items():
		if y > cutoff: phyloscanner_edges.append(x)

	return phyloscanner_edges


def get_tnet_edges(tnet_file):
	tnet_edges = []
	f = open(tnet_file)
	f.readline()
	for line in f.readlines():
		parts = line.split('\t')
		edge = parts[0]+'->'+parts[1]
		if edge not in tnet_edges:
			tnet_edges.append(edge)
		# print(edge)

	f.close()
	return tnet_edges


def get_mul_tnet_edges(tnet_file, cutoff):
	tnet_edges = []
	f = open(tnet_file)
	for line in f.readlines():
		parts = line.rstrip().split('\t')
		if int(parts[1]) >= cutoff:
			tnet_edges.append(parts[0])
		# print('M',parts)

	f.close()
	return tnet_edges


def get_summary_tnet_edges(tnet_file, cutoff):
	tnet_edges = []
	f = open(tnet_file)
	for line in f.readlines():
		parts = line.rstrip().split('\t')
		if int(parts[1]) > cutoff:
			tnet_edges.append(parts[0])
		# print('M',parts)

	f.close()
	return tnet_edges

def calculate_f1_score(TP, FP, FN):
	precision = TP/(TP+FP)
	recall = TP/(TP+FN)
	try:
		f1 = 2*(recall * precision) / (recall + precision)
	except ZeroDivisionError:
		f1 = 0

	return round(f1,3)

def generate_TP_FP_FN():
	folders = next(os.walk('result/'))[1]
	folders.sort()

	raxml_compare = open('raxml.all.result.csv', 'w+')
	raxml_compare.write('dataset,phy_tp,phy_fp,phy_fn,tnet_tp,tnet_fp,tnet_fn,tnet_50_tp,tnet_50_fp,tnet_50_fn,tnet_80_tp,tnet_80_fp,tnet_80_fn,tnet_100_tp,tnet_100_fp,tnet_100_fn\n')
	# truetree_compare = open('truetree.all.result.csv', 'w+')
	# truetree_compare.write('dataset,phy_tp,phy_fp,phy_fn,tnet_tp,tnet_fp,tnet_fn,tnet_50_tp,tnet_50_fp,tnet_50_fn,tnet_80_tp,tnet_80_fp,tnet_80_fn,tnet_100_tp,tnet_100_fp,tnet_100_fn\n')

	for folder in folders:
		print('Now in folder->',folder)
		cur_dir = 'result/' + folder + '/'
		result = []
		real_set = set(get_real_edges(cur_dir + 'real_network.txt'))
		# print(len(real_set))
		phyloscanner_set = set(get_phyloscanner_edges(cur_dir + 'phyloscanner/raxml.tree_collapsedTree.csv'))
		# phyloscanner_set = set(get_phyloscanner_edges(cur_dir + 'phyloscanner/true.tree_collapsedTree.csv'))
		# print(len(phyloscanner_set))
		TP = real_set & phyloscanner_set
		FP = phyloscanner_set - real_set
		FN = real_set - phyloscanner_set
		print('PScan TP',len(TP),'FP',len(FP),'FN',len(FN))
		result.append(len(TP))
		result.append(len(FP))
		result.append(len(FN))

		tnet_set = set(get_tnet_edges(cur_dir + 'raxml.tree.tnet'))
		# tnet_set = set(get_tnet_edges(cur_dir + 'true.tree.tnet'))
		# print(tnet_set)
		TP = real_set & tnet_set
		FP = tnet_set - real_set
		FN = real_set - tnet_set
		print('TNet TP',len(TP),'FP',len(FP),'FN',len(FN))
		result.append(len(TP))
		result.append(len(FP))
		result.append(len(FN))

		tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'raxml.tree.tnet.multiple', 50))
		# tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'true.tree.tnet.multiple', 50))
		# print(tnet_mul_set)
		TP = real_set & tnet_mul_set
		FP = tnet_mul_set - real_set
		FN = real_set - tnet_mul_set
		print('50_TNet TP',len(TP),'FP',len(FP),'FN',len(FN))
		result.append(len(TP))
		result.append(len(FP))
		result.append(len(FN))

		tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'raxml.tree.tnet.multiple', 80))
		# tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'true.tree.tnet.multiple', 80))
		# print(tnet_mul_set)
		TP = real_set & tnet_mul_set
		FP = tnet_mul_set - real_set
		FN = real_set - tnet_mul_set
		print('80_TNet TP',len(TP),'FP',len(FP),'FN',len(FN))
		result.append(len(TP))
		result.append(len(FP))
		result.append(len(FN))

		tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'raxml.tree.tnet.multiple', 100))
		# tnet_mul_set = set(get_mul_tnet_edges(cur_dir + 'true.tree.tnet.multiple', 100))
		# print(tnet_mul_set)
		TP = real_set & tnet_mul_set
		FP = tnet_mul_set - real_set
		FN = real_set - tnet_mul_set
		print('100_TNet TP',len(TP),'FP',len(FP),'FN',len(FN))
		result.append(len(TP))
		result.append(len(FP))
		result.append(len(FN))

		raxml_compare.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,result[0],result[1],result[2],result[3],result[4],
									result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14]))
		# truetree_compare.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,result[0],result[1],result[2],result[3],result[4],
									# result[5],result[6],result[7],result[8],result[9],result[10],result[11],result[12],result[13],result[14]))
		# break

	raxml_compare.close()
	# truetree_compare.close()
	print('TP FP FN FINISHED')

def generate_f1_score(type):
	f1_score = open('f1.' + type + '.result.csv', 'w+')
	f1_score.write('dataset,phy_f1,tnet_f1,tnet_50_f1,tnet_80_f1,tnet_100_f1\n')

	f = open(type + '.all.result.csv')
	f.readline()
	for line in f.readlines():
		parts = line.rstrip().split(',')
		# print(parts)
		result = []
		for i in range(5):
			TP = int(parts[i*3+1])
			FP = int(parts[i*3+2])
			FN = int(parts[i*3+3])
			result.append(calculate_f1_score(TP, FP, FN))
		
		f1_score.write('{},{},{},{},{},{}\n'.format(parts[0], result[0], result[1], result[2], result[3], result[4]))
		# break
	f.close()
	f1_score.close()
	print('FINISHED F1 FOR',type)

def tnet_RAxML_bootstrap(data_dir, folders):
	# Generating outputs
	for folder in folders:
		print('Now in folder->',folder)
		cur_dir = data_dir + '/' + folder + '/RAxML_output/'
		cur_file = cur_dir + 'RAxML_bootstrap.' + folder
		# print('Files here->',next(os.walk(cur_dir))[2])
		edge_dict = {}
		result = open('result/' + folder+ '/bootstrap.tnet.multiple', 'w+')

		bootstrap_all = open(cur_file)
		lines = bootstrap_all.readlines()
		for i in range(10):
			temp = open('bootstrap', 'w+')
			temp.write(lines[i])
			temp.close()

			# TNet with multiple sampling
			tnet_multiple('bootstrap', 'bootstrap', 10)
			# Reading .multiple file
			f = open('bootstrap.multiple')
			for line in f.readlines():
				parts = line.rstrip().split('\t')
				edge = parts[0]
				# print(parts)

				if edge in edge_dict:
					edge_dict[edge] += int(parts[1])
				else:
					edge_dict[edge] = int(parts[1])

			f.close()
			os.remove('bootstrap.multiple')

		# edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))
		# print(edge_dict)
		# last_key = list(edge_dict.keys())[-1]
		for x, y in edge_dict.items():
			result.write('{}\t{}\n'.format(x, y))
			# if x == last_key:
			# 	result.write('{}\t{}'.format(x, y))
			# else:
			# 	result.write('{}\t{}\n'.format(x, y))

		result.close()
		break



def main():
	# root_dir = '/home/saurav/research/Favites_data_from_sam/'

	# print('Please choose one of the following datasets->')
	# # print(next(os.walk(root_dir))[1])

	# dataset = 'SIR003'
	# print('You choose->',dataset)

	# data_dir = root_dir + dataset
	# folders = next(os.walk(data_dir))[1]

	cur_dir = 'seqgen/'
	folders = next(os.walk(cur_dir))[1]
	print('There are total {} data points in this dataset'.format(len(folders)))

	for folder in folders:
		# print(folder, create_phylo_multi_tree_input(folder))
		print(folder, phyloscanner_multi_tree(folder))

		# generate_outputs(data_dir, folders)
		# tnet_RAxML_bootstrap(data_dir, folders)
		# compare_outputs(folders)
		# generate_TP_FP_FN()
		# generate_f1_score('truetree')
		# break

	# real = set(get_real_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/SEIR01_sl250_mr025_nv10_1/real_network.txt'))
	# tnet_mul = set(get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/SEIR01_sl250_mr025_nv10_1/raxml.tree.tnet.multiple',80))
	# tnet_boot = set(get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/SEIR01_sl250_mr025_nv10_1/bootstrap.tnet.multiple',80))

	# TP = real & tnet_mul
	# FP = tnet_mul - real
	# FN = real - tnet_mul
	# print('80_TNet TP',len(TP),'FP',len(FP),'FN',len(FN))

	# TP = real & tnet_boot
	# FP = tnet_boot - real
	# FN = real - tnet_boot
	# print('80_TNet_boot TP',len(TP),'FP',len(FP),'FN',len(FN))




if __name__ == "__main__": main()