import pymysql


def testRead1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "select * from marksheet"
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "roll_no", "name", "phy", "chem", "math")
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
    connection.commit()
    connection.close()


def testRead3():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()

    sql = "select * from marksheet"
    # sql = "select * from marksheet where id = 1"
    # sql = "select * from marksheet where roll_no = 101"
    # sql = "select * from marksheet where name like 'a%'"
    # sql = "select * from marksheet where physics = 12"
    # sql = "select * from marksheet where chemistry = 34"
    # sql = "select * from marksheet where maths = 55"

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead4(id, roll_no, name, phy, chem, math):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()

    sql = 'select * from marksheet'
    if id != 0:
        sql += " where id = " + str(id)
    if roll_no != 0:
        sql += " where roll_no = " + str(roll_no)
    if name != '':
        sql += " where name like '" + name + "%'"
    if phy != 0:
        sql += " where phy = " + str(phy)
    if chem != 0:
        sql += " where chem = " + str(chem)
    if math != 0:
        sql += " where math = " + str(math)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead5(param={}):
    id = param.get('id', 0)
    roll_no = param.get('roll_no', 0)
    name = param.get('name', '')
    phy = param.get('phy', 0)
    chem = param.get('chem', 0)
    math = param.get('math', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if roll_no != 0:
        sql += " and roll_no = " + str(roll_no)
    if name != '':
        sql += " and name like '" + name + "%'"
    if phy != 0:
        sql += " and phy = " + str(phy)
    if chem != 0:
        sql += " and chem= " + str(chem)
    if math != 0:
        sql += " and math = " + str(math)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


def testRead6(param={}):
    id = param.get('id', 0)
    roll_no = param.get('rollNo', 0)
    name = param.get('name', '')
    phy= param.get('phy', 0)
    chem = param.get('chem', 0)
    math = param.get('math', 0)
    pageNo = param.get('pageNo', 0)
    pageSize = param.get('pageSize', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "select * from marksheet where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if roll_no != 0:
        sql += " and roll_no = " + str(roll_no)
    if name != '':
        sql += " and name like '" + name + "%'"
    if phy != 0:
        sql += " and physics = " + str(phy)
    if chem != 0:
        sql += " and chemistry = " + str(chem)
    if math != 0:
        sql += " and maths = " + str(math)

    if pageSize > 0:
        pageNo = (pageNo - 1) * pageSize
        sql += " limit " + str(pageNo) + ", " + str(pageSize)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
    connection.commit()
    connection.close()


# testRead1()
# testRead2()
# testRead3()
# testRead4(0, 0, '', 0, 0, 100)

param = {}
param['name'] = '%i'
param['roll_no'] = 0
param['pageNo'] = 1
param['pageSize'] = 1

# testRead5(param)

testRead6(param)