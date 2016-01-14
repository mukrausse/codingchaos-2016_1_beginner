#!/usr/bin/python

import sys
from string import ascii_uppercase 
dict = {}
alpha = []
beta = []
out = ""
j=0

f = open("BeispielAlphabet.txt", "r")

alpha = ascii_uppercase

for ch in f:
	beta.extend(ch.strip())
	j+1

for o in range(len(alpha)):
	dict[alpha[o]]=beta[o]

f.close()

for i in range(len(sys.argv)):
    if i != 0:
        #print(sys.argv[i])
	for c in sys.argv[i]:
		out+=str(dict[c.upper()])

	out+=" "

print(out)
