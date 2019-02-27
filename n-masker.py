"""
New and improved version of n_mask_script.py

Inputs: 

1. fasta file with all seqs (doesn't matter if there's a header)
2. vcf file with all variable loci for all reads (or only for the reads to be retained)
3. vcf file with the singular SNP of interest for each read to be retained
 
Outputs:

- Prints to console fasta file with all seqs identified in input 3 
  with SNP of interest encoded as the two alternate alleles (e.g. ...GCTC[C/T]GTAG... )
  and all other variable loci as "N"s

"""
from __future__ import print_function
import sys, re

#fasta file
file_object_1 = open(sys.argv[1])
#variable loci
file_object_2 = open(sys.argv[2])
#SNP of interest
file_object_3 = open(sys.argv[3])

#Regex expressions 
seq_catch = '\>\w+\_(\d+)'
vcf_catch = '(\d+)\_(\d+)\t(\w)\t(\w)'

tag_seq = {}
#Deals with headers if present
body = False

#Populates dictionary associating tag IDs with corresponding seqs 
for line in file_object_1:	
	seq_search = re.search(seq_catch, line)
	
	#If line starts with ">", store tag number
	if seq_search:
		body = True
		tag = seq_search.group(1)
	
	#Bc alternating line structure of fasta files, adds the line following ">" as the value to the dictionary
	elif body:
		tag_seq[tag] = list(line[:100])

#Replaces ALL variable loci with Ns
for line in file_object_2:
	vcf_search = re.search(vcf_catch, line)
	
	if vcf_search and int(vcf_search.group(2)) <= 100:
		tag_seq[vcf_search.group(1)][int(vcf_search.group(2))] = "N"

#Changes SNPs of interest to alternate alleles and outputs
for line in file_object_3:
	vcf_search = re.search(vcf_catch, line)
	
	if vcf_search:
		#Change prefix to suit your needs
		print(">Crot_{}_{}".format(vcf_search.group(1), vcf_search.group(2)))
		
		print_list = tag_seq[vcf_search.group(1)]
		print_list[int(vcf_search.group(2))] = "[{}\\{}]".format(vcf_search.group(3), vcf_search.group(4))
		
		for bp in print_list: print(bp, end = "")
		print("\n")
