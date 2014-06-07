#!/usr/bin/env python

# kopira samo prvo stevilo v posamezni vrstici
numbers = file('numbers.txt', 'w')
for i in file('euro2008full.txt', 'r').readlines():
    numbers.write(i.split()[0]+"\n")
numbers.close()
