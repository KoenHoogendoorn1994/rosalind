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

class Rabbit:

    def __init__(self,age,m):
        self.age = age
        self.m = m

    def reproduce(self):
        if self.age < self.m:
            if self.age > 0:
                return Rabbit(0,self.m)

    def grow(self):
        self.age += 1
    def die(self):
        if self.age == self.m:
            return True
        else:
            return False



def main(infile):
    for line in b.readinput(infile):
        data = line.strip().split()
        time = int(data[0])
        lifespan = int(data[1])
    rabbits = [Rabbit(0,lifespan)]
    print(len(rabbits))
    for t in range(time-1):
        for i in range(len(rabbits)-1,-1,-1):
            s= rabbits[i].reproduce()
            if s != None:
                rabbits.append(s)
            #print "check1"
            rabbits[i].grow()
            #print "check2"
            if rabbits[i].die():
                rabbits.pop(i)
                #print "DEAD"
        print len(rabbits)



if __name__ == "__main__":
    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')
    #b.simplewriteout(results)
            
