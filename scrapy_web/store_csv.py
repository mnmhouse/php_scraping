import csv
from urllib.request import  urlopen
from bs4 import  BeautifulSoup

#csv 存储csv例子
csvFile = open("download/test.csv",'w+')
try:
    writer =csv.writer(csvFile)
    writer.writerow(('nubmer','second','2times'))
    for i in range(10):
        writer.writerow((i,i+2,i*i))
finally:
    csvFile.close()

# 获取html表格并写入csv文件

html = urlopen("http://en.wikipedia.org/wiki/comparison_of_text_editors")
bsObj = BeautifulSoup(html)
# 主对比表格是当前页面上的第一个表格
table = bsObj.findAll('table',{"class":"wikitable"})[0]
rows = table.findAll('tr')
csvFile=open('editor.csv','wt',newline="",encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()