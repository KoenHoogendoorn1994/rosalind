#!/usr/bin/env python
# encoding: utf-8
"""
rosalind exercises
"""

# Imports
from __future__ import division
from sys import argv
import baselib as b
import itertools
from operator import itemgetter


def main(infile):
    # vars
    lines = []
    combis = []
    # processing
    for line in b.read(infile):
        # operation for every input line
        lines.append(line.strip())

    symbols = lines[0].replace(" ", "")
    stringlength = int(lines[1])
    for combination in itertools.product(symbols, repeat=stringlength):
        orderstring = ""
        for character in combination:
            orderstring += str(symbols.find(character))
        combis.append((combination, orderstring))
    s = sorted(combis, key=itemgetter(1))
    for elem in s:
        yield elem[0]


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
        
    b.simplewriteout(results)
