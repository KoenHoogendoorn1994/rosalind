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


def main(infile):
    # vars

    seqs = []
    # processing
    for record in b.read(infile, "fasta"):
        # operation for every input line
        seqs.append(record.seq)
    sequence = seqs[0]

    for size in range(4, 13, 2):
        for start in range(len(sequence)-size+1):
            end = start+size
            section = sequence[start:end]
            if section == b.revcomp(section):
                yield start+1, size


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
