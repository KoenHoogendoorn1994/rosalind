#!/usr/bin/env python
# encoding: utf-8
"""
rosalind exercises
"""

# Imports
from __future__ import division
import os
from sys import argv
import baselib as b
import math


def main(infile):
    # vars
    seqs = []

    # processing
    for record in b.read(infile, "fasta"):
        # operation for every input line
        seqs.append(record.seq)

    assembly = seqs[0]
    seqs.remove(assembly)
    min_overlap = int(math.floor(len(seqs[0])/2))
    max_overlap = len(seqs[0])
    while len(seqs) != 0:
        for elem in seqs:
            for length in range(max_overlap, min_overlap, -1):
                if elem.endswith(assembly[:length]):
                    assembly = elem + assembly[length:]
                    seqs.remove(elem)
                    break
                if assembly.endswith(elem[:length]):
                    assembly = assembly + elem[length:]
                    seqs.remove(elem)
                    break
            #print assembly
    print(assembly)
    return assembly


def overlap(seq1, seq2):
    min_len = int(math.ceil(max((len(seq1), len(seq2)))/2))

    if seq1[min_len:] in seq2:
        return -1
    elif seq1[:min_len] in seq2:
        return 1
    else:
        return False

if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
        
    b.simplewriteout(results)
