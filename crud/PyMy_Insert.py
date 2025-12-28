import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',password='root',db='PyMySql')
cursor = connection.cursor()
sql = "insert into marksheet values (6, 106, 'rubina', 65, 88, 28)"
cursor.execute(sql)
connection.commit()
connection.close()
print('data inserted successfully')
