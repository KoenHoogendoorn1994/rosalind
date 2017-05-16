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
    A = 0
    C = 1
    G = 2
    T = 3
    recordlength = []
    for header,record in b.parse_fasta(infile):
        recordlength.append(len(record))
    for elem in recordlength:
        if elem != recordlength[0]:
            exit("NOT EQUAL LENGTH")
    seqlen = recordlength[0]
    bases = [[0 for i in range(4)] for j in range(seqlen)]
    for header,record in b.parse_fasta(infile):
        for index, char in enumerate(record):
            if char == "A":
                bases[index][A] +=1
            if char == "C":
                bases[index][C] +=1
            if char == "G":
                bases[index][G] +=1
            if char == "T":
                bases[index][T] +=1
    
    return bases

def consensus(baselist):
    bases = {0:"A",1:"C",2:"G",3:"T"}
    consensus_seq = ""
    for i in range(len(baselist)):
        currentbase = 0
        winnerindex = 0
        for index, elem in enumerate(baselist[i]):
            if elem > currentbase:
                winnerindex = index
                currentbase = elem
        consensus_seq += bases[winnerindex]
    return consensus_seq

if __name__ == "__main__":

    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')
    cs = consensus(results)
    out_handle = open("output.txt","w")
    out_handle.write(cs)
    out_handle.write("\n")
    out_handle.write("A: ")
    for j in range(len(results)):
        out_handle.write(str(results[j][0]))
        out_handle.write(" ")
    out_handle.write("\n")
    out_handle.write("C: ")
    for k in range(len(results)):
        out_handle.write(str(results[k][1]))
        out_handle.write(" ")
    out_handle.write("\n")
    out_handle.write("G: ")
    for l in range(len(results)):
        out_handle.write(str(results[l][2]))
        out_handle.write(" ")
    out_handle.write("\n")
    out_handle.write("T: ")
    for m in range(len(results)):
        out_handle.write(str(results[m][3]))
        out_handle.write(" ")
    out_handle.close()
    #b.simplewriteout(results)
