import os
import operator
import get_results as gr

def generate_seqgen_tnet_multiple(folder):
	for i in range(10):
		input_file = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)
		out_file = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/Tnet.'  + str(i)
		# os.mkdir(out_file)
		if os.path.exists(out_file + '.multiple'):
			print('Already exists')
		else:
			gr.tnet_multiple(input_file, out_file, 100)


	edge_dict = {}
	result = open('result/'+folder+'/seqgen.tnet.multiple', 'w+')

	for i in range(10):
		# Reading .multiple file
		input_file = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/Tnet.'  + str(i)
		f = open(input_file + '.multiple')
		for line in f.readlines():
			parts = line.rstrip().split('\t')
			edge = parts[0]
			# print(parts)

			if edge in edge_dict:
				edge_dict[edge] += int(parts[1])
			else:
				edge_dict[edge] = int(parts[1])

		f.close()

	print(edge_dict)
	for x, y in edge_dict.items():
		result.write('{}\t{}\n'.format(x, y))

	result.close()


def create_seqgen_tnet_symmary(folder, th = 80):
	edge_dict = {}
	result = open('result/'+folder+'/seqgen.tnet.summary', 'w+')

	for i in range(10):
		# Reading .multiple file
		input_file = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/Tnet.'  + str(i)+ '.multiple'
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

	# print(edge_dict)
	edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))

	for x, y in edge_dict.items():
		result.write('{}\t{}\n'.format(x, y))

	result.close()


def all_rooted_trees_exist(folder):
	for i in range(10):
		rooted_tree = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)
		if not os.path.exists(rooted_tree):
			return False
		
	return True

def compare_tnet(folders):
	TP_FP_FN_file = open('SEIR01.phylo.multi.tnet.80.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('dataset,phylo_tp,phylo_fp,phylo_fn,phylo_multi_tp,phylo_multi_fp,phylo_multi_fn,tnet_tp,tnet_fp,tnet_fn,tnet_mul_tp,tnet_mul_fp,tnet_mul_fn,tnet_boot_tp,tnet_boot_fp,tnet_boot_fn\n')
	F1_file = open('SEIR01.phylo.multi.tnet.80.F1.csv', 'w+')
	F1_file.write('dataset,phylo_prec,phylo_rec,phylo_f1,phylo_multi_prec,phylo_multi_rec,phylo_multi_f1,tnet_prec,tnet_rec,tnet_f1,tnet_mul_prec,tnet_mul_rec,tnet_mul_f1,tnet_boot_prec,tnet_boot_rec,tnet_boot_f1\n')

	for folder in folders:
		# print('inside folder: ',folder, all_rooted_trees_exist(folder))
		if not all_rooted_trees_exist(folder):
			continue

		TP_FP_FN = []
		F1 = []

		real = set(gr.get_real_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/real_network.txt'))
		phylo = set(gr.get_phyloscanner_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/phyloscanner/raxml.tree_collapsedTree.csv'))
		phylo_multi = set(gr.get_phyloscanner_multi_tree_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/phyloscanner_multi_tree/seqgen_hostRelationshipSummary.csv'))
		tnet = set(gr.get_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/raxml.tree.tnet'))
		tnet_mul = set(gr.get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/raxml.tree.tnet.multiple',80))
		tnet_boot = set(gr.get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/seqgen.tnet.multiple', 800))


		TP = len(real & phylo)
		FP = len(phylo - real)
		FN = len(real - phylo)
		# print('Phylo TP',len(TP),'FP',len(FP),'FN',len(FN))
		precision = TP/(TP+FP)
		recall = TP/(TP+FN)
		f1 = 0
		try:
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		TP = len(real & phylo_multi)
		FP = len(phylo_multi - real)
		FN = len(real - phylo_multi)
		# print('Phylo_multi TP',len(TP),'FP',len(FP),'FN',len(FN))
		precision = TP/(TP+FP)
		recall = TP/(TP+FN)
		f1 = 0
		try:
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
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
		# print('TNet TP',len(TP),'FP',len(FP),'FN',len(FN))
		precision = TP/(TP+FP)
		recall = TP/(TP+FN)
		f1 = 0
		try:
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		TP = len(real & tnet_mul)
		FP = len(tnet_mul - real)
		FN = len(real - tnet_mul)
		# print('80_TNet_mul TP',len(TP),'FP',len(FP),'FN',len(FN))
		precision = TP/(TP+FP)
		recall = TP/(TP+FN)
		f1 = 0
		try:
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		TP = len(real & tnet_boot)
		FP = len(tnet_boot - real)
		FN = len(real - tnet_boot)
		# print('80_TNet_boot TP',len(TP),'FP',len(FP),'FN',len(FN))
		precision = TP/(TP+FP)
		recall = TP/(TP+FN)
		f1 = 0
		try:
			f1 = 2*(recall * precision) / (recall + precision)
		except ZeroDivisionError:
			f1 = 0

		TP_FP_FN.append(TP)
		TP_FP_FN.append(FP)
		TP_FP_FN.append(FN)
		F1.append(round(precision,3))
		F1.append(round(recall,3))
		F1.append(round(f1,3))

		# print(TP_FP_FN)
		# print(F1)
		TP_FP_FN_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5],TP_FP_FN[6],TP_FP_FN[7],TP_FP_FN[8],TP_FP_FN[9],TP_FP_FN[10],
							TP_FP_FN[11],TP_FP_FN[12],TP_FP_FN[13],TP_FP_FN[14]))
		F1_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5],F1[6],
							F1[7],F1[8],F1[9],F1[10],F1[11],F1[12],F1[13],F1[14]))

def main():
	cur_dir = 'seqgen/'
	folders = next(os.walk(cur_dir))[1]

	for folder in folders:
		print('inside folder: ',folder)
		create_seqgen_tnet_symmary(folder)

	# generate_seqgen_tnet_multiple('SEIR01_sl1000_mr025_nv20_20')
	# root_dir = '/home/saurav/research/Favites_data_from_sam/'

	# print('Please choose one of the following datasets->')
	# print(next(os.walk(root_dir))[1])

	# dataset = 'SEIR01'
	# print('You choose->',dataset)

	# data_dir = root_dir + dataset
	# folders = next(os.walk(data_dir))[1]
	# print('There are total {} data points in this dataset'.format(len(folders)))
	# compare_tnet(folders)

	# for folder in folders:
	# 	print('inside folder: ',folder, all_rooted_trees_exist(folder))
	# 	if not all_rooted_trees_exist(folder):
	# 		continue

	# 	real = set(gr.get_real_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/real_network.txt'))
	# 	tnet = set(gr.get_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/raxml.tree.tnet'))
	# 	tnet_mul = set(gr.get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/raxml.tree.tnet.multiple',80))
	# 	tnet_boot = set(gr.get_mul_tnet_edges('/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/'+folder+'/seqgen.tnet.multiple', 800))

	# 	TP = real & tnet
	# 	FP = tnet - real
	# 	FN = real - tnet
	# 	print('TNet TP',len(TP),'FP',len(FP),'FN',len(FN))

	# 	TP = real & tnet_mul
	# 	FP = tnet_mul - real
	# 	FN = real - tnet_mul
	# 	print('80_TNet_mul TP',len(TP),'FP',len(FP),'FN',len(FN))

	# 	TP = real & tnet_boot
	# 	FP = tnet_boot - real
	# 	FN = real - tnet_boot
	# 	print('80_TNet_boot TP',len(TP),'FP',len(FP),'FN',len(FN))

if __name__ == "__main__": main()