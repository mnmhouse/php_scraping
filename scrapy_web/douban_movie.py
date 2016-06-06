# -- coding: utf-8 --
import urllib
from urllib.request import urlopen
from urllib.request import Request
import time
from bs4 import BeautifulSoup
BaseUrl = "https://book.douban.com/tag/%E7%94%B5%E5%BD%B1?start=0&type=T"
j=1
# 设置始末页码
for i in range(0, 98):
  url = "https://book.douban.com/tag/%E7%94%B5%E5%BD%B1?start="+str(i*20)+"&type=T"
  headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

  opener = urllib.request.build_opener()
  opener.addheaders = [headers]
  # page = opener.open(url).read()
  #解决BeautifulSoup中文乱码问题

  page = urlopen(url).read()
  soup = BeautifulSoup(page, from_encoding="gb18030")
  # print("requet page"+page)
  item_lists = soup.find_all("li", {"class":"subject-item"})

  for item in item_lists:
    #选择想要的点击率
    ration = item.find("span",{"class":"rating_nums"})
    if float(ration.string)>9.0:

      content = item.find("div",{"class":"info"})

      title = content.find("h2").find("a").get_text()

      des =content.find("p")
      print(des)
      line2 =des.get_text()
      print(line2)

      f = open('movie.md', 'a')
      f.write("###"+" "+title+"\t"+"<"+line2+">"+"\t"+ "star"+str(ration.get_text())+"\n")
      f.close()
      j+=1