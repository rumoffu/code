#!/usr/bin/env python
# Opens text file "3038html.txt" and prints out pubchem_id \t common_name, 1 set per line
# Based on line with cgi and cid= and &loc
'''
'''
b = []
for line in open("3038html.txt"):
	line = line.strip()
	if line.find("cgi") != -1: #gets lines with the pubchem_id which comes after cgi
		b.append(line)
s = ""
for piece in b:
	# pubchem id is http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=7476&loc=ec_rcs
	cid = piece.find("cid=") # pubchem_id starts after cid= 
	loc = piece.find("&loc") # pubchem_id ends before &loc
	if cid != -1: # piece has pubchem_id
		s += piece[cid+4:loc] # get pubchem_id which starts 4 after cid and ends before loc
		print s
		s = ""


# Opens ODL_pubchem.txt that has ODL# \t pubchemid
# will print out pubchemid
prefix = "http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid="
for line in open("pubchemids.txt"):
	output = prefix + line.strip()
	print output.strip()

#!/usr/bin/env python
# Opens a file called "pubchemid_sites.txt" in the same directory. 
# opens all sites of that list, and extracts compound name 
# and prints the pubchem ID then a tab then the common name
'''
5365976	allyl alpha-ionone
21149427	CAMPHOLENE ACETATE
643779	citral
7720	2-ethylhexanol
'''
import re
import urllib2

for site in open("pubchemid_sites.txt"):
	cid = site.find("cid=") + 4 #only get what's after cid=
	pubchemid = site[cid:].strip()
	if pubchemid != "":
		response = urllib2.urlopen(site)
		page_source = response.read()
		response.close()
		left = page_source.find("<title>")
		right = page_source.find("</title>")
		print pubchemid + "\t" + page_source[left+7:right-10]
	else:
		print "\t"
