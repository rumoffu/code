#!/usr/bin/env python

# Opens ODL_pubchem.txt that has ODL# \t pubchemid
# will print out pubchemid
prefix = "http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid="
for line in open("pubchemids.txt"):
	output = prefix + line.strip()
	print output.strip()

