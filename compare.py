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
	result = open('outputs/'+folder+'/seqgen.tnet.multiple', 'w+')

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


def create_seqgen_tnet_symmary(folder, th = 50):
	edge_dict = {}
	result = open('outputs/'+folder+'/seqgen.tnet.summary.' + str(th), 'w+')

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

def create_undirected_seqgen_tnet_symmary(folder, th = 50):
	edge_dict = {}
	result = open('outputs/'+folder+'/undirected.seqgen.tnet.summary.' + str(th), 'w+')

	for i in range(10):
		# Reading .multiple file
		tnet_edges = {}
		input_file = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/Tnet.'  + str(i)+ '.multiple'
		f = open(input_file)
		for line in f.readlines():
			parts = line.rstrip().split('\t')
			edge = parts[0]
			parts_edge = edge.rstrip().split('->')
			rev_edge = parts_edge[1]+ '->' +parts_edge[0]
			# print(edge,rev_edge)

			if edge in tnet_edges:
				tnet_edges[edge] += int(parts[1])
			elif rev_edge in tnet_edges:
				tnet_edges[rev_edge] += int(parts[1])
			else:
				tnet_edges[edge] = int(parts[1])

		f.close()

		# tnet_edges = dict(sorted(tnet_edges.items(), key=operator.itemgetter(1),reverse=True))
		# print(i,tnet_edges)

		for edge, count in tnet_edges.items():
			if count < th: continue
			print(edge, count)
			parts_edge = edge.rstrip().split('->')
			rev_edge = parts_edge[1]+ '->' +parts_edge[0]
			if edge in edge_dict:
				edge_dict[edge] += 1
			elif rev_edge in edge_dict:
				edge_dict[rev_edge] += 1
			else:
				edge_dict[edge] = 1

	edge_dict = dict(sorted(edge_dict.items(), key=operator.itemgetter(1),reverse=True))
	# print(edge_dict)
	for x, y in edge_dict.items():
		result.write('{}\t{}\n'.format(x, y))

	result.close()


def all_rooted_trees_exist(folder):
	for i in range(10):
		rooted_tree = 'seqgen/'+folder+'/RAxML_'+ str(i)+'/RAxML_rootedTree.' + str(i)
		if not os.path.exists(rooted_tree):
			return False
		
	return True

def compare_directed(folders):
	TP_FP_FN_file = open('directed.phylo.tnet.50.th_5.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('dataset,phylo_tp,phylo_fp,phylo_fn,phylo_multi_tp,phylo_multi_fp,phylo_multi_fn,tnet_tp,tnet_fp,tnet_fn,tnet_mul_tp,tnet_mul_fp,tnet_mul_fn,tnet_boot_tp,tnet_boot_fp,tnet_boot_fn\n')
	F1_file = open('directed.phylo.tnet.50.th_5.F1.csv', 'w+')
	F1_file.write('dataset,phylo_prec,phylo_rec,phylo_f1,phylo_multi_prec,phylo_multi_rec,phylo_multi_f1,tnet_prec,tnet_rec,tnet_f1,tnet_mul_prec,tnet_mul_rec,tnet_mul_f1,tnet_boot_prec,tnet_boot_rec,tnet_boot_f1\n')

	for folder in folders:
		print('inside folder: ',folder)

		TP_FP_FN = []
		F1 = []

		real = set(gr.get_real_edges('outputs/'+folder+'/real_network.txt'))
		phylo = set(gr.get_phyloscanner_edges('outputs/'+folder+'/phyloscanner/raxml.tree_collapsedTree.csv'))
		phylo_multi = set(gr.get_phyloscanner_multi_tree_edges('outputs/'+folder+'/phyloscanner_multi_tree/seqgen_hostRelationshipSummary.csv', 5))
		tnet = set(gr.get_tnet_edges('outputs/'+folder+'/raxml.tree.tnet'))
		tnet_mul = set(gr.get_mul_tnet_edges('outputs/'+folder+'/raxml.tree.tnet.multiple',50))
		tnet_boot = set(gr.get_summary_tnet_edges('outputs/'+folder+'/seqgen.tnet.summary.50', 5))


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

		TP = len(real & phylo_multi)
		FP = len(phylo_multi - real)
		FN = len(real - phylo_multi)
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

		TP = len(real & tnet_mul)
		FP = len(tnet_mul - real)
		FN = len(real - tnet_mul)
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

		TP = len(real & tnet_boot)
		FP = len(tnet_boot - real)
		FN = len(real - tnet_boot)
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

		# print(TP_FP_FN)
		# print(F1)
		TP_FP_FN_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5],TP_FP_FN[6],TP_FP_FN[7],TP_FP_FN[8],TP_FP_FN[9],TP_FP_FN[10],
							TP_FP_FN[11],TP_FP_FN[12],TP_FP_FN[13],TP_FP_FN[14]))
		F1_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5],F1[6],
							F1[7],F1[8],F1[9],F1[10],F1[11],F1[12],F1[13],F1[14]))


def compare_undirected(folders):
	TP_FP_FN_file = open('undirected.phylo.tnet.50.th_5.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('dataset,phylo_tp,phylo_fp,phylo_fn,phylo_multi_tp,phylo_multi_fp,phylo_multi_fn,tnet_tp,tnet_fp,tnet_fn,tnet_mul_tp,tnet_mul_fp,tnet_mul_fn,tnet_boot_tp,tnet_boot_fp,tnet_boot_fn\n')
	F1_file = open('undirected.phylo.tnet.50.th_5.F1.csv', 'w+')
	F1_file.write('dataset,phylo_prec,phylo_rec,phylo_f1,phylo_multi_prec,phylo_multi_rec,phylo_multi_f1,tnet_prec,tnet_rec,tnet_f1,tnet_mul_prec,tnet_mul_rec,tnet_mul_f1,tnet_boot_prec,tnet_boot_rec,tnet_boot_f1\n')

	for folder in folders:
		print('inside folder: ',folder)

		TP_FP_FN = []
		F1 = []

		real = set(gr.get_real_edges('outputs/'+folder+'/real_network.txt'))
		phylo = set(gr.get_phyloscanner_edges('outputs/'+folder+'/phyloscanner/raxml.tree_collapsedTree.csv'))
		phylo_multi_with_complex = set(gr.get_phyloscanner_multi_tree_edges_with_complex('outputs/'+folder+'/phyloscanner_multi_tree/seqgen_hostRelationshipSummary.csv', 5))
		tnet = set(gr.get_tnet_edges('outputs/'+folder+'/raxml.tree.tnet'))
		tnet_mul = set(gr.get_mul_tnet_edges('outputs/'+folder+'/raxml.tree.tnet.multiple', 50))
		tnet_boot = set(gr.get_summary_tnet_edges('outputs/'+folder+'/undirected.seqgen.tnet.summary.50', 5))

		TP = len(intersection(real, phylo))
		FP = len(minus(phylo,real))
		FN = len(minus(real,phylo))
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

		TP = len(intersection(real, phylo_multi_with_complex))
		FP = len(minus(phylo_multi_with_complex,real))
		FN = len(minus(real,phylo_multi_with_complex))
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

		TP = len(intersection(real, tnet))
		FP = len(minus(tnet,real))
		FN = len(minus(real,tnet))
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

		TP = len(intersection(real, tnet_mul))
		FP = len(minus(tnet_mul,real))
		FN = len(minus(real,tnet_mul))
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

		TP = len(intersection(real, tnet_boot))
		FP = len(minus(tnet_boot,real))
		FN = len(minus(real,tnet_boot))
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

		# print(TP_FP_FN)
		# print(F1)
		TP_FP_FN_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5],TP_FP_FN[6],TP_FP_FN[7],TP_FP_FN[8],TP_FP_FN[9],TP_FP_FN[10],
							TP_FP_FN[11],TP_FP_FN[12],TP_FP_FN[13],TP_FP_FN[14]))
		F1_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(folder,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5],F1[6],
							F1[7],F1[8],F1[9],F1[10],F1[11],F1[12],F1[13],F1[14]))


def intersection(a,b):
	intersection = []
	for b_i in b:
		parts_b = b_i.rstrip().split('->')
		b_i_r = parts_b[1]+ '->' +parts_b[0]
		if b_i in a: intersection.append(b_i)
		if b_i_r in a: intersection.append(b_i_r)

	return set(intersection)

def minus(a,b):
	minus = set(a)

	for b_i in b:
		parts_b = b_i.rstrip().split('->')
		b_i_r = parts_b[1]+ '->' +parts_b[0]
		if b_i in a and b_i in minus: minus.remove(b_i)
		if b_i_r in a and b_i_r in minus: minus.remove(b_i_r)

	return minus

def seqgen_compare_directed(th = 50):
	cur_dir = 'seqgen/'
	folders = next(os.walk(cur_dir))[1]
	folders.sort()

	TP_FP_FN_file = open('directed.seqgen.tnet.80.th_'+ str(th) +'.TP_FP_FN.csv', 'w+')
	TP_FP_FN_file.write('dataset,phylo_tp,phylo_fp,phylo_fn,phylo_complex_tp,phylo_complex_fp,phylo_complex_fn,tnet_tp,tnet_fp,tnet_fn\n')
	F1_file = open('directed.seqgen.tnet.80.th_'+ str(th) +'.F1.csv', 'w+')
	F1_file.write('dataset,phylo_prec,phylo_rec,phylo_f1,phylo_complex_prec,phylo_complex_rec,phylo_complex_f1,tnet_prec,tnet_rec,tnet_f1\n')

	for folder in folders:
		print('inside folder: ',folder)

		TP_FP_FN = []
		F1 = []

		real = set(gr.get_real_edges('outputs/'+folder+'/real_network.txt'))
		phylo = set(gr.get_phyloscanner_multi_tree_edges('outputs/'+folder+'/phyloscanner_multi_tree/seqgen_hostRelationshipSummary.csv', 5))
		phylo_with_complex = set(gr.get_phyloscanner_multi_tree_edges_with_complex('outputs/'+folder+'/phyloscanner_multi_tree/seqgen_hostRelationshipSummary.csv', 5))
		tnet = set(gr.get_summary_tnet_edges('outputs/'+folder+'/seqgen.tnet.summary.80', 5))

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

		TP = len(real & phylo_with_complex)
		FP = len(phylo_with_complex - real)
		FN = len(real - phylo_with_complex)
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

		TP_FP_FN_file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(folder,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
							TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5],TP_FP_FN[6],TP_FP_FN[7],TP_FP_FN[8]))
		F1_file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(folder,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5],F1[6],
							F1[7],F1[8]))

def main():
	seqgen_compare_directed(50)
	# cur_dir = 'seqgen/'
	# folders = next(os.walk(cur_dir))[1]
	# folders.sort()
	# match = 'mr025'
	# match2 = 'mr0125'
	# new_folders = []

	# for folder in folders:
	# 	if match in folder or match2 in folder:
	# 		new_folders.append(folder)

	# print(new_folders)
	# print(len(new_folders))
	# compare_tnet(new_folders)
	# compare_directed(folders)

	# TP_FP_FN_file = open('tnet.different.TP_FP_FN.csv', 'w+')
	# TP_FP_FN_file.write('dataset,tnet_50_tp,tnet_50_fp,tnet_50_fn,tnet_80_tp,tnet_80_fp,tnet_80_fn,tnet_100_tp,tnet_100_fp,tnet_100_fn\n')
	# F1_file = open('tnet.different.F1.csv', 'w+')
	# F1_file.write('dataset,tnet_50_prec,tnet_50_rec,tnet_50_f1,tnet_80_prec,tnet_80_rec,tnet_80_f1,tnet_100_prec,tnet_100_rec,tnet_100_f1\n')

	# for folder in folders:
	# 	print('inside folder: ',folder)
	# 	create_seqgen_tnet_symmary(folder, 80)
	# 	create_undirected_seqgen_tnet_symmary(folder, 80)
	# 	# break

	# generate_seqgen_tnet_multiple('SEIR01_sl1000_mr025_nv20_20')
	# root_dir = '/home/saurav/research/Favites_data_from_sam/'

	# print('Please choose one of the following datasets->')
	# print(next(os.walk(root_dir))[1])

	# 
	# print('You choose->',dataset)

	# data_dir = root_dir + dataset
	# folders = next(os.walk(data_dir))[1]
	# print('There are total {} data points in this dataset'.format(len(folders)))
	# compare_tnet(folders)

	# for folder in folders:
	# 	real = set(gr.get_real_edges('outputs/'+folder+'/real_network.txt'))
	# 	tnet_mul_50 = set(gr.get_mul_tnet_edges('outputs/'+folder+'/raxml.tree.tnet.multiple',50))
	# 	tnet_mul_80 = set(gr.get_mul_tnet_edges('outputs/'+folder+'/raxml.tree.tnet.multiple',80))
	# 	tnet_mul_100 = set(gr.get_mul_tnet_edges('outputs/'+folder+'/raxml.tree.tnet.multiple',100))

	# 	TP_FP_FN = []
	# 	F1 = []

	# 	TP = len(real & tnet_mul_50)
	# 	FP = len(tnet_mul_50 - real)
	# 	FN = len(real - tnet_mul_50)

	# 	try:
	# 		precision = TP/(TP+FP)
	# 		recall = TP/(TP+FN)
	# 		f1 = 2*(recall * precision) / (recall + precision)
	# 	except ZeroDivisionError:
	# 		precision = 0
	# 		recall = 0
	# 		f1 = 0

	# 	TP_FP_FN.append(TP)
	# 	TP_FP_FN.append(FP)
	# 	TP_FP_FN.append(FN)
	# 	F1.append(round(precision,3))
	# 	F1.append(round(recall,3))
	# 	F1.append(round(f1,3))

	# 	TP = len(real & tnet_mul_80)
	# 	FP = len(tnet_mul_80 - real)
	# 	FN = len(real - tnet_mul_80)

	# 	try:
	# 		precision = TP/(TP+FP)
	# 		recall = TP/(TP+FN)
	# 		f1 = 2*(recall * precision) / (recall + precision)
	# 	except ZeroDivisionError:
	# 		precision = 0
	# 		recall = 0
	# 		f1 = 0

	# 	TP_FP_FN.append(TP)
	# 	TP_FP_FN.append(FP)
	# 	TP_FP_FN.append(FN)
	# 	F1.append(round(precision,3))
	# 	F1.append(round(recall,3))
	# 	F1.append(round(f1,3))

	# 	TP = len(real & tnet_mul_100)
	# 	FP = len(tnet_mul_100 - real)
	# 	FN = len(real - tnet_mul_100)

	# 	try:
	# 		precision = TP/(TP+FP)
	# 		recall = TP/(TP+FN)
	# 		f1 = 2*(recall * precision) / (recall + precision)
	# 	except ZeroDivisionError:
	# 		precision = 0
	# 		recall = 0
	# 		f1 = 0

	# 	TP_FP_FN.append(TP)
	# 	TP_FP_FN.append(FP)
	# 	TP_FP_FN.append(FN)
	# 	F1.append(round(precision,3))
	# 	F1.append(round(recall,3))
	# 	F1.append(round(f1,3))

	# 	TP_FP_FN_file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(folder,TP_FP_FN[0],TP_FP_FN[1],TP_FP_FN[2],
	# 					TP_FP_FN[3],TP_FP_FN[4],TP_FP_FN[5],TP_FP_FN[6],TP_FP_FN[7],TP_FP_FN[8]))
	# 	F1_file.write('{},{},{},{},{},{},{},{},{},{}\n'.format(folder,F1[0],F1[1],F1[2],F1[3],F1[4],F1[5],F1[6],F1[7],F1[8]))

if __name__ == "__main__": main()