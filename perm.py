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
import itertools
import math


def main(infile):
    # vars

    # processing
    for line in b.read(infile):
        k = int(line.strip())
        initial = [x+1 for x in range(k)]
        print k
        s = open("output.txt", "w")
        s.write(str(math.factorial(k)) + "\n")
        for index, permutation in enumerate(itertools.permutations(initial)):
            for elem in permutation:
                s.write(str(elem) + " ")
            if index < math.factorial(k)-1:
                s.write("\n")


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
    b.simplewriteout(results)
