#!/usr/bin/env python3
import argparse

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--verion', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
print(args)

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]
    
    for line in lines:
        print(line.strip()[::-1])
 
#parse the arguments

#read the file, reverse the contents and print