from Bio import SeqIO
import shutil, os

def create_cdc_fasta_file():
	files = next(os.walk('CDC/fasta_files'))[2]
	print(len(files))

	records = []

	for file in files:
		records.extend(list(SeqIO.parse('CDC/fasta_files/'+ file, 'fasta')))

	print(len(records))
	for i in range(len(records)):
	    # print(records[i].id)
	    parts = records[i].id.rstrip().split('_')
	    # print(parts[0] + '_N' + str(i))
	    records[i].id = parts[0] + '_N' + str(i)
	    records[i].name = ''
	    records[i].description = ''

	print(records)
	SeqIO.write(records, "CDC/AA_to_BX.fasta", "fasta")


def create_raxml_output(bootstrap):
	input_file = '/home/saurav/research/tnet_vs_pscanner/CDC/AA_to_BX.fasta'
	output_dir = '/home/saurav/research/tnet_vs_pscanner/CDC/RAxML_output'
	cmd = 'raxmlHPC -f a -m GTRGAMMA -p 12345 -x 12345 -s {} -w {} -N {} -n cdc -k'.format(input_file, output_dir, bootstrap)
	print(cmd)

	# os.system(cmd)

def create_cdc_phyloscanner_input(input_folder, output_folder):
	for i in range(20):
		rooted_tree = input_folder + '/RAxML_rootedTree.' + str(i)
		rename_tree = output_folder + '/CDC_bootstrap.InWindow_'+ str(1000+i*100) +'_to_'+ str(1099+i*100) +'.tree'
		shutil.copy(rooted_tree, rename_tree)

def create_bootstrap_tree_files(bootstrap_trees_file,output_folder):
	f = open(bootstrap_trees_file)
	tree_list = f.readlines()
	
	for i in range(len(tree_list)):
		file = open(output_folder + '/cdc.bootstrap.' + str(i), 'w')
		file.write(tree_list[i])

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
	os.system(cmd)
	# print(cmd)


def main():
	# create_cdc_fasta_file()
	create_raxml_output(20)
	# create_bootstrap_tree_files('CDC/RAxML_output/RAxML_bootstrap.cdc','CDC/RAxML_output/bootstrap_trees')
	# root_bootstrap_tree_files('CDC/RAxML_output/bootstrap_trees','/home/saurav/research/tnet_vs_pscanner/CDC/tnet_input')
	# create_cdc_phyloscanner_input('CDC/tnet_input','CDC/phyloscanner_input')
	# run_phyloscanner_cdc('CDC/phyloscanner_input','CDC/phyloscanner_output')


	


if __name__ == "__main__": main()
