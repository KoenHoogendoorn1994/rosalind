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
    expected = 0
    chances = [1,1,1,0.75,0.5,0]
    # processing
    for line in b.read(infile):
        # operation for every input line
        popnums = line.strip().split(" ")
        for index, elem in enumerate(popnums):
            expected += (chances[index]*int(elem)*2)


    # returning results
    print expected
    return expected


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
