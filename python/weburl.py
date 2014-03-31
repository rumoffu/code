#!/usr/bin/env python
# Description
'''
Example input:
7476	4-acetylanisole
7478	4-anisic acid
7501	Styrene

Example output:

'''
from selenium import webdriver
import urllib2


def main():
  driver = webdriver.Firefox()
  #link = "http://www.sigmaaldrich.com/catalog/product/aldrich/137499?lang=en&region=US"
  link = "http://www.sigmaaldrich.com/catalog/ProductDetail.do?N5=SEARCH_CONCAT_PNO&N4=245542|ALDRICH"
  
  #print content
  printLink(link)
  return
  # Get Redirected link content
  driver.get(link)
  #Wait for it to load
  while(link == driver.current_url):
    time.sleep(1)
  redir_url = driver.current_url
  
  #print content
  printLink(link)

  
def printLink(link):
  response = urllib2.urlopen(link)
  page_source = response.read()
  response.close()
  print page_source

if __name__ == '__main__':
  main()


