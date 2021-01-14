import random


class EmployeeWageBuilder:
    def __init__(self):
        self.check_attendence = 0

    check_attendence = random.randint(0, 1)
    if check_attendence == 1:
        print('Employee is present')
    else:
        print('Employee is absent')


