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
  #driver = webdriver.Chrome()
  #driver = webdriver.Chrome(executable_path="/home/sirus/opt/chromedriver")
  driver = webdriver.Firefox()
  #link = "http://www.sigmaaldrich.com/catalog/product/aldrich/137499?lang=en&region=US"
  link = "http://www.sigmaaldrich.com/catalog/ProductDetail.do?N5=SEARCH_CONCAT_PNO&N4=245542|ALDRICH"
  
  #print content
  #printLink(link)

  # Get Redirected link content
  driver.get(link)
  #Wait for it to load
  count = 0
  while(link == driver.current_url):
    time.sleep(1)
    print 'loading %s' % count
    count =+ 1
  redir_url = driver.current_url
  
  #print content
  #printLink(link)

  driver.quit()
  #driver.close()
  #print 'close'
  
def executeJS(link):
  driver = webdriver.Firefox()
  driver.get(link)
  resp = driver.execute_script("return 5")
  print resp
  driver.quit()
  
def printLink(link):
  response = urllib2.urlopen(link)
  page_source = response.read()
  response.close()
  print page_source

if __name__ == '__main__':
  main()


