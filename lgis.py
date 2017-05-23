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
import math


def main(infile):
    # vars
    lines = []
    population = []
    desc = []
    asc = ""
    # processing
    for line in b.read(infile):
        lines.append(line.strip())
    popsize = lines[0]
    for elem in lines[1:]:
        for character in elem.replace(" ", ""):
            population.append(int(character))

    print(population)
    p = [0] * len(population)
    m = [0] * (len(population)+1)

    l = 0
    for i in range(0, len(population)-1):
        lo = 1
        hi = l
        while lo <= hi:
            mid = int(math.ceil((lo+hi)/2))
            if population[m[mid]] < population[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newl = lo
        p[i] = m[newl - 1]
        m[newl] = i

        if newl > l:
            l = newl

    s = [0]*l
    k = m[l]
    for i in range(k-1, 0):
        s[i] = population[k]
        k = p[k]

    return s


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')

    b.simplewriteout(results)
