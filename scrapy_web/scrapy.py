from  urllib.request import  urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

url = "http://www.pythonscraping.com/pages/warandpeace.html"
#
# import  re
#
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://www.sina.com')
#     bsObj = BeautifulSoup(html)
#     for link  in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:


# BeautifulSoup 的使用
# html = urlopen("http://www.sina.com")
# print(BeautifulSoup(html).h1)

# Error handle

def getText(url):
    try:
        html =urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html)
        title = bsObj.body.h1
    except AttributeError as e:
        print(e)
        return  None
    return title

title = getText("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not find")
else:
    print(title)

# BeautifulSoup Find all,findAll
def iteratorText():
    htmlAll = urlopen(url)
    bsObject = BeautifulSoup(htmlAll)
    listtest = bsObject.findAll("span",{"class":"red"})
    for item  in listtest:
        print(item.getText())

iteratorText()