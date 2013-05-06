#!/usr/bin/env python

# Opens ODL_pubchem.txt that has ODL# \t pubchemid
# will print out pubchemid
for line in open("ODL_pubchem.txt"):
	cols = line.split('\t')	
	print cols[1].strip()

