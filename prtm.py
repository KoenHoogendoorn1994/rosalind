#!/usr/bin/env python
# encoding: utf-8
"""
rosalind exercises
"""

# Imports
from __future__ import division
from sys import argv
import baselib as b


def main(infile):
    # vars
    massdict = {"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
                "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
                "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
                "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
                "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}
    sequence = ""
    total_mass = float(0)
    # processing
    for line in b.read(infile):
        sequence += line.strip()
    for character in sequence:
        total_mass += massdict[character]

    # returning results
    return round(total_mass, 3)


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
    print(results)
    b.simplewriteout(results)
