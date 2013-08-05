#!/usr/bin/env python
# Opens text file "3038html.txt" and prints out pubchem_id \t common_name, 1 set per line
# Based on line with cgi and cid= and &loc
# Extracts common_name based on <title> </title>
'''
7476	4-acetylanisole
7478	4-anisic acid
7501	Styrene
'''
b = []
for line in open("3038html.txt"):
	line = line.strip()
	if line.find("cgi") != -1: #gets lines with the pubchem_id which comes after cgi
		b.append(line)
prefix = "http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid="
import re
import urllib2
for piece in b:
	# pubchem id is http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=7476&loc=ec_rcs
	cid = piece.find("cid=") # pubchem_id starts after cid= 
	loc = piece.find("&loc") # pubchem_id ends before &loc
	if cid != -1: # piece has pubchem_id
		pubchem_id = piece[cid+4:loc] # get pubchem_id which starts 4 after cid and ends before loc
		if pubchem_id != "": # avoid ODL molecules that do not have pubchem_id
			link = prefix + pubchem_id
			response = urllib2.urlopen(link)
			page_source = response.read()
			response.close() # close the link
			left = page_source.find("<title>")
			right = page_source.find("</title>")
			print pubchem_id + "\t" + page_source[left+7:right-10] # remove <title> and remove " - PubChem"
