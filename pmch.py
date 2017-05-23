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
    sequence = seqs[0]

    cgn = sequence.count("C")
    aun = sequence.count("U")

    s = math.factorial(cgn) * math.factorial(aun)
    return s


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
        
    b.simplewriteout(results)
