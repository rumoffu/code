#!/usr/bin/env python
'''
Opens "list" which has a list of pubchem sites
http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=66955
and finds the common name and outputs the common name
'''
from bs4 import BeautifulSoup
import re
import urllib2

#response = urllib2.urlopen("http://chem.sis.nlm.nih.gov/chemidplus/ProxyServlet?objectHandle=DBMaint&actionHandle=default&nextPage=jsp/chemidheavy/ResultScreen.jsp&ROW_NUM=0&TXTSUPERLISTID=0022771444")
#response = urllib2.urlopen("http://chem.sis.nlm.nih.gov/chemidplus/")
#response = urllib2.urlopen("http://chem.sis.nlm.nih.gov/chemidplus/ProxyServlet?objectHandle=DBMaint&actionHandle=default&nextPage=jsp/chemidheavy/ResultScreen.jsp&ROW_NUM=0&TXTSUPERLISTID=0029414560")
#response = urllib2.urlopen("http://pubchem.ncbi.nlm.nih.gov/")
#response = urllib2.urlopen("https://www.google.com/")
#response = urllib2.urlopen("http://www.packtpub.com/article/web-scraping-with-python-part-2")

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
#if "<title>" in page_source:
#	print line

#soup = BeautifulSoup(page_source)

#contact = {}
#for line in soup.findAll("table"):
#	print line
#	s = line.find('span')
#	if s:
#	print s

#t = soup.findAll('')
#print t

