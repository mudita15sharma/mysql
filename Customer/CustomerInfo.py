import pymysql

class CustomerInfo:

    def nextPk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "select max(id) from CustomerInfo"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def adding(self, data):
        id = CustomerInfo.nextPk(self)
        C_name = data['C_name']
        Loc = data['Loc']
        Con_Num = data['Con_Num']
        Dob = data['Dob']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "insert into customerinfo values(%s, %s, %s, %s, %s)"
        data = (id, C_name, Loc, Con_Num, Dob)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def updating(self, data):
        id = data['id']
        C_name = data['C_name']
        Loc= data['Loc']
        Con_Num= data['Con_Num']
        Dob= data['Dob']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "update customerinfo set C_name = %s, Loc = %s, Con_Num = %s, Dob= %s where id = %s"
        data = (C_name,Loc,Con_Num,Dob, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data updated successfully')

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "delete from customerinfo where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data deleted successfully')

    def get(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "select * from customerinfo where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
        connection.commit()
        connection.close()


    def search(self, data):
        C_name = data.get('C_name', '')
        Con_Num = data.get('Con_Num', 0)
        pageNo = data.get('pageNo', 0)
        pageSize = data.get('pageSize', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "select * from customerinfo where 1=1"
        if C_name != '':
            sql += " and C_name = '" + C_name + "'"
        if Con_Num != 0:
            sql += " and Con_Num = " + str(Con_Num)
        if (pageSize > 0):
            pageNo = (pageNo - 1) * pageSize
            sql += " limit " + str(pageNo) + ", " + str(pageSize)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
        connection.commit()
        connection.close()


    def find(self, Loc):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='PyMySql')
        cursor = connection.cursor()
        sql = "select * from customerinfo where Loc = %s"
        data = (Loc)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4])
        connection.commit()
        connection.close()
