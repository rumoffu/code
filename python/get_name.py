#!/usr/bin/env python
'''
Opens "list" which has a list of pubchem sites
http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=66955
and finds the common name and outputs the common name
'''
from bs4 import BeautifulSoup
import re
import urllib2

#response = urllib2.urlopen("http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=7476")
for site in open("list"):
	response = urllib2.urlopen(site)
	page_source = response.read()
	response.close()
#print page_source
#for line in page_source:
	left = page_source.find("<title>")
	right = page_source.find("</title>")
	print page_source[left+7:right-10]
