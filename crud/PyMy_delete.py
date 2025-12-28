import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root',password='root',db='PyMySql')
cursor = connection.cursor()
sql = "delete from marksheet where id = 3"
cursor.execute(sql)
connection.commit()
connection.close()
print('data deleted successfully')
