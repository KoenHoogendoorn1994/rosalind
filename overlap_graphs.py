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
    overlaps = []
    records = []

    # processing
    for record in b.read(infile, "fasta"):
        # operation for every input line
        records.append(record)
    print len(records)
    for i in range(len(records)):
        for j in range(len(records)):

            seq1 = records[i].seq
            seq2 = records[j].seq
            # print records[i].name,records[j].name
            if overlap(seq1, seq2) and seq1 != seq2:
                #print "DING"
                overlaps.append((records[i].name, records[j].name))

    # returning results
    return overlaps


def overlap(seq_a, seq_b, k=3):
    if seq_a[-k:] == seq_b[0:k]:
        #print seq_a[-k:]
        return True
    else:
        return False


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
