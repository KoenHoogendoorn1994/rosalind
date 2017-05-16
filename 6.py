#!/usr/bin/env python
# encoding: utf-8
"""
rosalind excercises
"""
from __future__ import division
import os
from sys import argv
import baselib as b


def main(infile):
    hmmdist = 0
    lines = []
    for line in b.readinput(infile):
        lines.append(line.strip())
    
    for i in range(len(lines[0])):
        if lines[0][i] != lines[1][i]:
            hmmdist +=1
    result = hmmdist
    return result


if __name__ == "__main__":

    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
