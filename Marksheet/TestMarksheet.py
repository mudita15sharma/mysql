from MarksheetModel import MarksheetModel


def testAdd():
    params = {}
    # params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'abc'
    params['phy'] = 70
    params['chem'] = 67
    params['math'] = 79

    model = MarksheetModel()
    model.add(params)


def testUpdate():
    params = {}
    params['id'] = 8
    params['roll_no'] = 108
    params['name'] = 'ooo'
    params['phy'] = 70
    params['chem'] = 67
    params['math'] = 79

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(8)


def testGet():
    model = MarksheetModel()
    model.get(7)


def testFindByRollNo():
    model = MarksheetModel()
    model.findByRoll(105)


def testSearch():
    params = {}
    params['name'] = 'abc'
    # params['roll_no'] =
    # params['pageNo'] = 1
    # params['pageSize'] = 0
    model = MarksheetModel()
    model.search(params)


testAdd()
testUpdate()
testGet()
testFindByRollNo()
testSearch()
testDelete()