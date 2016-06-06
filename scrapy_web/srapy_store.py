import  os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup


# 获取一个图片文件地址,下载保存到为logo.jpg
html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
print(imageLocation)
urlretrieve(imageLocation,"logo.jpg")

# 获取页面上所有src属性的文件
downloadDirectory = "download"
baseUrl = "http://pythonscraping.com"

def getAsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url ="http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("wwww."):
        url="http://"+source[4:]
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None

    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("wwww.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory+path
    directory = os.path.dirname(path)

    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

downloadList = bsObj.findAll(src=True)

for down in  downloadList:
    fileUrl = getAsoluteURL(baseUrl,down["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))

