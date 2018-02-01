#Usage: python getDomains.py IP

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import csv
import sys
IP=str(sys.argv[1])
webPage='https://www.whois.com/whois/'
browser = webdriver.PhantomJS(executable_path=r'/home/sm8kk/Webscraping/phantomjs-1.9.8-linux-x86_64/bin/phantomjs')
browser.get(webPage)
search=browser.find_element_by_name('query')
search.send_keys(IP)
search.submit()
pagesource = browser.page_source
bsObj = BeautifulSoup(pagesource, "html.parser")
bsObj.find(id="registryData").contents[0]
print bsObj.find(id="registryData").contents[0].split("\n")
browser.quit()
