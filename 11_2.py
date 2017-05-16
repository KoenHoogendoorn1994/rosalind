#!/usr/bin/env python
# encoding: utf-8
"""
bed_from_genbank.py
grab the gene records from a genbank file (edit for other record types).
- requires:  biopython
"""
from __future__ import division
import os
from sys import argv
import baselib as b

def main(infile):
    for line in b.readinput(infile):
        data = line.strip().split()
        time = int(data[0])
        lifespan = int(data[1])

    time = 6
    lifespan = 6
    rabbits = [1,1]
    change = [1,0]
    for i in range(3,time+1):
        newrabbits = (rabbits[i-2]-change[i-3])*2
        change.append(newrabbits)
        print change
        if len(rabbits) >= lifespan:
            dead = rabbits[-1] - (change[i-lifespan])
        else:
            dead = 0
        rabbits.append(change[-1]-dead)
##        if i < 40:
##            print i,rabbits
        #print i,rabbits
    return [int(rabbits[-1])]

        



if __name__ == "__main__":
    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')
    b.simplewriteout(results)
            
