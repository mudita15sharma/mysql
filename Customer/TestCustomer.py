from CustomerInfo import CustomerInfo

def testAdd():
    params = {}
    params['id'] = 4
    params['C_name'] ='dfhv'
    params['Loc'] = 'Dhar'
    params['Con_Num'] = 5654
    params['Dob'] = 4576

    model = CustomerInfo()
    model.adding(params)


# testAdd()

def testupdate():
    params = {}
    params['id'] = 5
    params['C_name'] = 'def'
    params['Loc'] = 'Dhar'
    params['Con_Num'] = 67557
    params['Dob'] = 1221

    model = CustomerInfo()
    model.updating(params)

# testupdate()

def testDel():
    model = CustomerInfo()
    model.delete(1)

testDel()

def testget():
    model = CustomerInfo()
    model.get(6)
# testget()


def testSearch():
    params = {}
    params['C_name'] = 'dfhv'
    # params['Con_Num'] =
    # params['pageNo'] = 1
    # params['pageSize'] = 0
    model = CustomerInfo()
    model.search(params)

# testSearch()

def testfind():
    model = CustomerInfo()
    model.find('Dhar')

# testfind()