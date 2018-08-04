import pypyodbc

conn = pypyodbc.win_connect_mdb('D:\\student.mdb')
cur = conn.cursor()
sql = "INSERT INTO stu values(123, 'zhangsan')"
cur.execute(sql)
cur.commit()
conn.close()
