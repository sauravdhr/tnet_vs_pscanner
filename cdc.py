from Bio import SeqIO
import os


def main():
	files = next(os.walk('CDC'))[2]
	print(len(files))

	records = []

	for file in files:
		records.extend(list(SeqIO.parse('CDC/'+ file, 'fasta')))

	print(len(records))
	for record in records:
	    print(record.id)
	    print(record.seq)
	#     # seqlist.append(record)

	SeqIO.write(records, "CDC_AA_to_BX.fasta", "fasta")


if __name__ == "__main__": main()
