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
    shortestseq = seqs[0]
    for elem in seqs:
        if len(elem) < len(shortestseq):
            shortestseq = elem

    longestmotif = ""

    for i in range(len(shortestseq)):
        for j in range(i, len(shortestseq)+1):
            for index, elem in enumerate(seqs):
                region = shortestseq[i:j]
                if region not in elem:
                    break
                elif index == len(seqs)-1:
                    if len(region) > len(longestmotif):
                        longestmotif = region

    # returning results
    print longestmotif
    return True


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
