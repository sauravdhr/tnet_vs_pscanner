import os
from ete3 import Tree

# root_dir = '/home/saurav/research/Favites_data_from_sam/'

# print('Please choose one of the following datasets->')
# print(next(os.walk(root_dir))[1])

# dataset = 'SIR003'
# print('You choose->',dataset)

# data_dir = root_dir + dataset
# folders = next(os.walk(data_dir))[1]
# print('There are total {} data points in this dataset'.format(len(folders)))

# for folder in folders:
# 	print('Now in folder->',folder)
# 	input_file = data_dir + '/' + folder + '/FAVITES_output/error_free_files/transmission_network.txt'
# 	# out_dir = data_dir + '/' + folder + '/clean_data/'
# 	out_dir = '/home/saurav/Dropbox/Research/tnet_vs_pscanner/result/' + folder + '/real_network.txt'
	# print('Files here->',next(os.walk(cur_dir))[2])

	# t = Tree(input_file)
	# for node in t.traverse("preorder"):
	# 	temp = node.name.split('|')
	# 	if len(temp) == 3:
	# 		node.name = temp[1] + '_' + temp[0]
	# 	# print(node.name)

	# output_file = out_dir +folder + '.true.tree'
	# # print(output_file)
	# os.remove(output_file)
	# t.write(outfile = output_file, format=1)

	# os.system('cp {} {}'.format(input_file, out_dir))
	# break

trees = open('RAxML_bootstrap.SEIR01_sl250_mr025_nv10_1')
lines = trees.readlines()
for i in range(10):
	temp = open('boot', 'w+')
	temp.write(lines[i])
	temp.close()
	cmd = 'raxmlHPC -f I -m GTRGAMMA -t RAxML_bestTree.SEIR01_sl250_mr025_nv10_1 -n tnet.rooted'

# t = Tree('bootstrap1.tre')
# for node in t.traverse("preorder"):
# 	# temp = node.name.split('|')
# 	# if len(temp) == 3:
# 	# 	node.name = temp[1] + '_' + temp[0]
# 	if node.is_root():
# 		print(node.name, node.is_root())

# print(t)
# output_file = 'rename.tre'
# # print(output_file)
# print(t.get_tree_root())
# t.write(outfile = output_file, format=9)