import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',password='root',db='PyMySql')
cursor = connection.cursor()
sql = "update marksheet set name = 'rubi' where id = 6"
cursor.execute(sql)
connection.commit()
connection.close()
print('data updated successfully')
