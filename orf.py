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
import re


def main(infile):
    # vars

    # processing
    for record in b.read(infile, "fasta"):
        orfs = []
        sequence = record.seq
        for orf in range(1, 7):
            prot = b.translatedna(sequence, orf)
            # print(prot)
            for index, elem in enumerate(prot):
                if elem == "M":
                    matches = re.findall(r"^M[\w]*\*", prot[index:])
                    if len(matches) != 0:
                        orfs.append(matches[0][:-1])

        return set(orfs)
if __name__ == "__main__":
    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
