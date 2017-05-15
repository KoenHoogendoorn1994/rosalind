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

    # processing
    for line in b.simpleread(infile):
        # operation for every input line
        continue

    # returning results
    return True


if __name__ == "__main__":

    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')
        
    # b.simplewriteout(results)
