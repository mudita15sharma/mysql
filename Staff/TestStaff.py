from Staff_Info import Staff_Info

def test_Add():
    params = {}
    params['id'] = 0
    params['name'] = input("Enter Employee Name: ")
    params['join_dat'] = input("Enter Employee Date: ")
    params['dep_div'] = input("Enter Employee Dep: ")
    params['prev_emp'] = input("Enter Employee Prev. Emp.: ")

    model = Staff_Info()
    model.add(params)

test_Add()