import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "insert into marksheet values(8, 108, 'abc', 34, 48, 38)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (9, 109, 'xyz', 78, 67, 56)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert3(id, rollNo, name, physics, chemistry, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert4(data={}):
    id = data['id']
    rollNo = data['rollNo']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, rollNo, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


# testInsert1()
# testInsert2()
# testInsert3(10, 110, 'pqr', 89, 77, 67)

params = {}
params['id'] = 3
params['rollNo'] = 103
params['name'] = 'hhff'
params['physics'] = 10
params['chemistry'] = 90
params['maths'] = 50

print(params)
testInsert4(params)