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




def parse_fasta(filename):
    s = open(filename)
    header = ""
    record = ""
    inrecord = False
    for line in s:
        if inrecord and not line.startswith(">"):
            record +=(line.strip())
        elif inrecord and line.startswith(">"):
            yield header,record
            inrecord = False
            header = ""
            record = ""
        if line.startswith(">"):
            header = line.strip()
            inrecord = True
    yield header,record

    
def readinput(file1):
    s = open(file1)
    for line in s:
        yield line.strip()
    s.close()

def main(infile):
    winner = 0
    recname = ""
    for header,record in parse_fasta(infile):
        rec_len = len(record)
        cg_cont = (record.count("C")+record.count("G"))/rec_len
        print header, rec_len, round(cg_cont,5)
        if cg_cont > winner:
            winner = round(cg_cont,8)
            recname = header
        
    
            
    result = recname, winner*100
    return result


def writeout(results):
    out_file = open("output.txt","w")
    print results
    for elem in results:
        out_file.write(str(elem).lstrip(">"))
        out_file.write("\n")
    out_file.close()


if __name__ == "__main__":

    if len(argv) > 1 :
        results = main(argv[1])
    else:
        results = main('sample.txt')

    writeout(results)
