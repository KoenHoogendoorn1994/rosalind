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
    reference = seqs.pop(0)

    for elem in seqs:
        reference = reference.replace(elem, "")

    return b.translate(reference)


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
        
    b.simplewriteout(results)
