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
    strings = []
    matchpos = ""
    for line in b.readinput(infile):
        strings.append(line)
    mainstr = strings[0]
    substr = strings[1]

    for i in range(0,len(mainstr)-1):
        if substr == mainstr[i:i+len(substr)]:
            matchpos+= str(i+1)+ " "
    result = matchpos.strip()
    return result


if __name__ == "__main__":

    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
