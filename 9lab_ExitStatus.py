#!/usr/bin/env python3
import argparse
import sys

#build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--verion', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
   print(f"Error: {err}")
   sys.exit(2)
#https://www.cyberciti.biz/faq/linux-bash-exit-status-set-exit-statusin-bash/
#except:
#    print(f"Testing")
else:
#print(args)
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:args.limit]
        
        for line in lines:
            print(line.strip()[::-1])
#finally:
#    print(f"Finally")
#parse the arguments

#read the file, reverse the contents and print