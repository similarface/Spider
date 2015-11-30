__author__ = 'similarface'


import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory="/Users/similarface/Downloads/temp"
baseUrl="http://pythonscraping.com"

def getAbsoluteURL(baseURL,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url=source[4:]
        url="http://"+source
    else:
        url=baseUrl+"/"+source
    if baseURL not in url:
        return None
    return url

'''
获取下载路径
'''
def getDownloadPath(baseURl,absoluteURL,downloadDirectory):
    path=absoluteURL.replace("www.","")
    path=path.replace(baseUrl,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)
    print(directory+">")
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html)
downloadList=bsObj.findAll(src=True)

for download in downloadList:
    fileUrl=getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)

        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))