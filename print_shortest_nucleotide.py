#! /usr/bin/python3

seq=["AAA", "T", "ATGTATG", "ATGTA", "AA", "TGTGTTGGTGAGTC", "ATGC"]

shortest=seq[0]

for i in seq:
   if  len(i)<len(shortest):
        shortest=i

print(" " + shortest + " ")
