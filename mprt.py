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
import urllib2
import re


def main(infile):
    # vars
    motif = re.compile(r"N[^P][ST][^P]")

    # processing
    for line in b.read(infile):
        # operation for every input line
        record = ""
        prot_id = line.strip()
        url = "http://www.uniprot.org/uniprot/{}.fasta".format(prot_id)
        response = urllib2.urlopen(url)
        startpos = []
        for elem in response.readlines():
            if not elem.startswith(">"):
                record += elem.strip()
        for index, character in enumerate(record):
            if character == "N" and index <= len(record)-4:
                if motif.match(record[index:index+4]):
                    startpos.append(str(index+1))
        if len(startpos) > 0:
            # print prot_id, startpos
            yield prot_id, startpos


if __name__ == "__main__":

    if len(argv) > 1:
        results = main(argv[1])
    else:
        results = main('sample.txt')
    with open("output.txt", "w") as out_file:
        for result in results:
            out_file.write(result[0] + "\n")
            outstr = " ".join(result[1])+"\n"
            out_file.write(outstr)

        #b.simplewriteout(results)
