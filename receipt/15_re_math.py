#!/usr/bin/env python
import os
import glob
import json
import shutil
import math

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")
#receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

#for path in receipts:
for path in glob.iglob('./new/receipt-[0-9]*.json'):
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    #name = path.split("/")[2]
    #"./new/receipts-1.json".split('/') => ['.', 'new', 'receipts-1.json'] => Lay phan tu [2] ~ -1
    #destination = f"./processed/{name}"
    destination = path.replace('new','processed')
    shutil.move (path, destination)
    print(f"move '{path}' to '{destination}'")

#print("Receipt subtotal: $%.2f" % subtotal)
print(f"Receipt subtotal: ${subtotal}")
print(f"Receipt subtotal: ${math.ceil(subtotal)}")
print(f"Receipt subtotal: ${math.floor(subtotal)}")
print(f"Receipt subtotal: ${round(subtotal,2)}")