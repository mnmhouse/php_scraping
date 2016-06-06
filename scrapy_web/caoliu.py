# -- coding: utf-8 --
import urllib
from urllib.request import urlopen
from urllib.request import Request
import threading
import time
import sys
from bs4 import BeautifulSoup
# reload(sys)
# sys.setdefaultencoding('utf8')
BaseUrl = "http://t66y.com/"
j=1
# 设置始末页码
for i in range(1, 98):
  #  #默认str会把字符串变成unicode，所以开头必须用sys来重置
  url = "http://t66y.com/thread0806.php?fid=22&search=&page="+str(i)
  headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')


# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)
#                          AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
#            "Accept":"text/html,application/xhtml+xml,application/xml;
#                      q=0.9,image/webp,*/*;q=0.8"}
  opener = urllib.request.build_opener()
  opener.addheaders = [headers]
  page = opener.open(url).read()
  #解决BeautifulSoup中文乱码问题

  soup = BeautifulSoup(page, from_encoding="gb18030")
  # print("requet page"+page)
  counts = soup.find_all("td", {"class":"tal f10 y-style"})

  for count in counts:
    #选择想要的点击率
    if int(count.string)>50:
      time.sleep(2)
      videoContainer = count.previous_sibling.previous_sibling.previous_sibling.previous_sibling
      video = videoContainer.find("h3")
      print("Downloading link "+ str(j))
      line1 = (video.get_text())
      line2 = BaseUrl+video.a.get('href')
      line3 = "view **" + count.string + "** "
      print(line1)
      f = open('cao.md', 'a')
      f.write("\n"+"###"+" "+line1+"\n"+"<"+line2+">"+"\n"+line3+ "  "+ "page"+str(i)+"\n")
      f.close()
      j+=1