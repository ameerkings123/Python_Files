Nucleotides=['A','C','T','G']

def validateSeq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


rndDNAstr='gtcaa'

print(validateSeq(rndDNAstr)) 
