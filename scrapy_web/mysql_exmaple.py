import  pymysql
# 连接对象
conn = pymysql.connect(host='127.0.0.1',unix_socket='/tmp/mysql.sock',user='root',passwd='house',db='mysql')
cur=conn.cursor()#光标对象
cur.execute("USE scraping")#使用数据库
cur.execute('SELECT * FROM pages')
print(cur.fetchall())
cur.close()
conn.close()