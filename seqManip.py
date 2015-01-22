# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 11:27:37 2015

@author: Marisa_29
"""
# define a DNA sequence (taken from 
# https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)
"""*** Sequence Manipulation Exercise ***
- Create a new Python script (text file)
- At the beginning of the script, define a DNA sequence (taken from 
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)
- Print the length of the sequence to the screen along with text explaining 
the value
- Create and store the RNA equivalent of the sequence, then print to screen.
- Create and store the reverse complement of your sequence, then print to 
screen.
- Extract the bases corresponding to the 13rd and 14th codons from the 
sequence, then print them to the screen.
- Create a function to translate the nucleotide sequence to amino acids 
using the vertebrate mitochondrial genetic code (available from 
https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt).
- Translate the sequence and print it to the screen.
- Be sure you've added comments to explain what this script is and what the 
different bits of code mean.
- Save this script as "seqManip.py" and commit it to your class GitHub repo.
"""

dna = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggctg"
# dna = "..' will define dna as whatever is inside the parenthesis
#print(dna) will print the dna sequence
dna_length = len(dna)
print"\n" "this is the length of the DNA sequence:" 
print(dna_length)
#will print the dna sequence length (620)
rna = (dna.replace("t","u"))
#replaced all the t with u to make the RNA equivalent of the DNA sequence
#make sure to use the correct case
rna = "aaaagcuaucgggcccauaccccaaacauguugguuaaaccccuuccuuugcuaauuaauccuuacgcuaucuccaucauuaucuccagcuuagcccugggaacuauuacuacccuaucaagcuaccauugaauguuagccugaaucggccuugaaauuaacacucuagcaauuauuccucuaauaacuaaaacaccucacccucgagcaauugaagccgcaacuaaauacuucuuaacacaagcagcagcaucugccuuaauucuauuugcaagcacaaugaaugcuugacuacuaggagaaugagccauuaauacccacauuaguuauauuccaucuauccuccucuccaucgcccuagcgauaaaacugggaauugcccccuuucacuucugacuuccugaaguccuacaaggauuaaccuuacaaaccggguuaaucuuaucaacaugacaaaaaaucgccccaauaguuuuacuuauucaacuaucccaaucuguagaccuuaaucuaauauuauuccucggcuuacuuucuacaguuauuggcggaugaggagguauuaaccaaacccaaauucguaaaguccuagcauuuucaucaaucgcccaccuaggcug"
#sequence stored as rna
print(rna)
dna = dna.replace("c", "x") # x is the placeholder for c
dna = dna.replace("t", "y") # y is a placeholder for t
dna = dna.replace("a", "t") # converts a to u
dna = dna.replace("g", "c") # converts g to c
dna = dna.replace("x", "g") # gets rid of the placeholder x and replaces it with a g
dna = dna.replace("y", "a") # gets rid of the placeholder y and replaces it with an a
reverse_comp=dna[::-1]
print"\n" "this is the reverse complement of the DNA sequence: "
print(reverse_comp)
print"\n" "these are the bases corresponding to the 13th and 14th codons of the DNA sequence: "
print (dna[36:42])
trimmed_dna = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggc"
#removed the last two bases from orig. dna seq
#The Vertebrate Mitochondrial Genetic Code:
translation_table = {
'ATA':'M', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'*', 'AGG':'*',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'W', 'TGG':'W'}

#Taken from: http://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi?mode=c#SG2
Length_trimmed_dna_sequence = len(trimmed_dna)
print("Length of trimmed dna sequence: " + str(Length_trimmed_dna_sequence))

# A function that takes dna as input and then outputs a protein sequence
def translate_dna(dna):   
    protein = ""
# Using range function with a 3 part argument
# 0 refers to starting position (python starts at 0 not 1)
# 618 refers to the ending position ()
# 3 refers to step size  
    for start in range(0,618,3):
        codon = dna[start:start+3]
# the retrieval of the aminio acid that corresponds to a codon
        aminoacid = translation_table.get(codon)
# protein gets the appropriate amino acid added to it       
        protein = protein + aminoacid
    return protein
print"\n" "this is the dna sequence translated into amino acids "
print(translate_dna("AAAAGCTATCGGGCCCATACCCCAAACATGTTGGTTAAACCCCTTCCTTTGCTAATTAATCCTTACGCTATCTCCATCATTATCTCCAGCTTAGCCCTGGGAACTATTACTACCCTATCAAGCTACCATTGAATGTTAGCCTGAATCGGCCTTGAAATTAACACTCTAGCAATTATTCCTCTAATAACTAAAACACCTCACCCTCGAGCAATTGAAGCCGCAACTAAATACTTCTTAACACAAGCAGCAGCATCTGCCTTAATTCTATTTGCAAGCACAATGAATGCTTGACTACTAGGAGAATGAGCCATTAATACCCACATTAGTTATATTCCATCTATCCTCCTCTCCATCGCCCTAGCGATAAAACTGGGAATTGCCCCCTTTCACTTCTGACTTCCTGAAGTCCTACAAGGATTAACCTTACAAACCGGGTTAATCTTATCAACATGACAAAAAATCGCCCCAATAGTTTTACTTATTCAACTATCCCAATCTGTAGACCTTAATCTAATATTATTCCTCGGCTTACTTTCTACAGTTATTGGCGGATGAGGAGGTATTAACCAAACCCAAATTCGTAAAGTCCTAGCATTTTCATCAATCGCCCACCTAGGC"))
