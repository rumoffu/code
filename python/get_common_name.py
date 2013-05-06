#!/usr/bin/env python
# Opens a file called "pubchemid_sites.txt" in the same directory 
# opens all sites of that list, and extracts compound name and prints
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
