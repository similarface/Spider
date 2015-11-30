#coding:utf-8
__author__ = 'similarface'
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen
import _thread as thread
#commercial-tests-table test-list

import socketserver

socketserver.ThreadingTCPServer

html=urlopen("https://www.invitae.com/en/physician/category/CAT000015/")
soup=BeautifulSoup(html)

print(soup.prettify())
#Hereditary Cancer Test List
#commercial-tests-table test-list

#Hereditary Cancer Gene List
#commercial-tests-table gene-list
"".endswith('.csv')