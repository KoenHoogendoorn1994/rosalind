#!/usr/bin/env python
# encoding: utf-8
"""
rosalind base functions
"""

# Imports
from __future__ import division


def simplewriteout(output):
    with open("output.txt", "w") as out:
        if type(output) in [str, int, float, bool, long]:
            # print output
            out.write(str(output))
        else:
            for elem in output:
                # print elem
                out.write(elem[0]+" "+elem[1]+"\n")
    return


def read(inname, filetype='txt'):
    with open(inname, 'r') as infile:
        if filetype == "txt":
            for line in infile:
                yield line

        if filetype.lower() in ["fasta", "fa"]:
            in_record = False

            for line in infile:
                if in_record:
                    if line.startswith(">"):
                        yield (record)
                        in_record = False
                    else:
                        record.seq += line.strip()
                if line.startswith(">"):
                    record = FastaRecord(line.strip()[1:])
                    in_record = True
            yield record

class FastaRecord:

    def __init__(self, recordname, seq=""):
        self.name = recordname
        self.seq = seq


