#!/usr/bin/env python
# encoding: utf-8
"""
rosalind base functions
"""

# Imports
from __future__ import division


def simplewriteout(output):
    with open("output.txt", "w") as out:
        if type(output) in [str, int, float, bool]:
            print output
            out.write(str(output))
        else:
            for elem in output:
                for elem2 in elem:
                    out.write(str(elem2))
                print elem
                # out.write(elem[0]+" "+elem[1]+"\n")
                out.write("\n")
    return


def read(inname, filetype='txt'):
    with open(inname, 'r') as infile:
        if filetype == "txt":
            for line in infile:
                yield line

        if filetype.lower() in ["fasta", "fa"]:
            in_record = False

            for line in infile:
                if in_record:
                    if line.startswith(">"):
                        yield (record)
                        in_record = False
                    else:
                        record.seq += line.strip()
                if line.startswith(">"):
                    record = FastaRecord(line.strip()[1:])
                    in_record = True
            yield record


def translate(dna, orf=1, includestop=False):
    aa_dict = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
               "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
               "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
               "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
               "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
               "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
               "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
               "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
               "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
               "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
               "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
               "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
               "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
               "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
               "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
               "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

    protein = ""
    if orf > 3:
        orf = orf - 3
        dna = revcomp(dna)

    if "U" not in dna:
        dna = dna.replace("T", "U")
    dna = dna[orf - 1:]

    for i in range(0, len(dna), 3):

        if i + 3 <= len(dna):
            triplet = dna[i:i + 3]

        if includestop:
            protein += aa_dict[triplet]
        elif aa_dict[triplet] != "*":
            protein += aa_dict[triplet]

    return protein


def revcomp(dna):
    dna = reversed(dna)
    newdna = ""
    replace_dict = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for character in dna:
        newdna += replace_dict[character]

    return newdna


class FastaRecord:
    def __init__(self, recordname, seq=""):
        self.name = recordname
        self.seq = seq
