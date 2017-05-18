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

k=0
def main(infile):
    # vars

    # processing
    for line in b.read(infile):
        global k
        k = int(line.strip())
        initial = [x+1 for x in range(k)]
        for permutation in itertools.permutations(initial):
            yield permutation


def output(generator,k):
    with open("output.txt", "w") as out:





if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
        print(results)
     global k
    output(results,k)
    # b.simplewriteout(results)
