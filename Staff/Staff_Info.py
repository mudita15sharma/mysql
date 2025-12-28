import pymysql


class Staff_Info:

    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host ='localhost', port = 3306, user = 'root', password= 'root', db = 'PyMySql')
        cursor = connection.cursor()
        sql = 'select max(id) from staff_info'
        cursor.execute(sql)
        results = cursor.fetchall()
        for data in results:
            if data is not None:
                print(data[0], '\t',data[1],'\t', data[2],'\t', data[3], '\t', data[4])
                pk = data[0]
            else :
                print('Table is empty!')
        connection.commit()
        connection.close()
        return pk + 1

    def add(self,data):
        id = Staff_Info.nextpk(self)
        name = data('name')
        join_dat = data['join_dat']
        dep_dev = data['dep_div']
        prev_emp = data['prev_emp']
        connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password= 'root', db = 'PyMySql')
        cursor= connection.cursor()
        sql = "insert into staff values('%s', '%s', '%s', '%s', '%s' )"
        data = (id, name, join_dat, dep_dev, prev_emp)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Inserted Successfully!!")




