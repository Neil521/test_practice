#coding=utf-8
import pymssql
conn=pymssql.connect(host='localhost:1434',user='sa',password='123456',database='Test',charset='GBK')
cur=conn.cursor()
if not cur:
    raise Exception('failed')
else:print('success')
sql='select * from student'
cur.execute(sql)
results=cur.fetchall()
for result in results:
    print(result)
update='update student set sbirthday=dateadd(year,-90,sbirthday)'
try:
    #执行
    cur.execute(update)
    #提交数据库
    conn.commit()
except:
    #错误回滚
    conn.rollback()
print()
cur.execute(sql)
results=cur.fetchall()
for result in results:
    print(result)
conn.close()
