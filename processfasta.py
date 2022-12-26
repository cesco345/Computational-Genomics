#! /usr/bin/python3

import sys
import getopt

#myfile =sys.argv[1]

try:
    f = open(myfile.fa)
except IOError:
    print("File %s does not exist!!" % myfile.fa)

o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts = {}
seqlen = 0

for k, v in o:
    opts[k] = v

if '-l' in opts.keys():
    if int(opts['l']) < 0 :
        print("Length of sequence should be positive!"); sys.exit(0)
    seqlen = opts['-l']
