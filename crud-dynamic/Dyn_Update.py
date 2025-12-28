import pymysql


def testUpdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = 104, name = 'ppp', phy = 99, chem = 99, math = 99 where id = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, phy = %s, chem = %s, math = %s where id = %s"
    data = (100, 'xyy', 72, 72, 26, 2)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate3(roll_no, name, phy, chem, math, id):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, phy = %s, chem = %s, math = %s where id = %s"
    data = (roll_no, name, phy, chem, math, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')


def testUpdate4(data):
    id = data['id']
    roll_no = data['roll_no']
    name = data['name']
    phy = data['phy']
    chem = data['chem']
    math = data['math']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
    cursor = connection.cursor()
    sql = "update marksheet set roll_no = %s, name = %s, phy = %s, chem = %s, math = %s where id = %s"
    data = (roll_no, name, phy, chem, math, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data updated successfully')

# testUpdate1()
# testUpdate2()
# testUpdate3(103, 'pqr', 89, 77, 67, 3)

params = {}
params['id'] = 4
params['roll_no'] = 104
params['name'] = 'klj'
params['phy'] = 100
params['chem'] = 100
params['math'] = 100

testUpdate4(params)