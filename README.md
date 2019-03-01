# `n-masker` for GT-Seq

This script modifies a fasta file for the creation of primers to use with GT-Seq by coding for alternate SNPs of interest and masking other variable base pairs in the reads as "N"s.

## Inputs

1. A fasta file with all reads or RADtags (doesn't matter if there's a header)
2. A vcf file with all SNPs for all loci
3. A vcf file with each targeted SNP 

## Output

Prints to console only the reads associated with the SNPs listed in input 3 as a fasta file with SNP of interest encoded as the two alternate SNPs (e.g. ...GCTC[C/T]GTAG... ) and all other variable base pairs as "N"s

## Example use

```python n-masker.py all_loci.fasta all_snps.vcf GTSeq_488.snps.vcf```
