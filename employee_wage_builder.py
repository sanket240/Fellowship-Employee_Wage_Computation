import random
IS_FULL_TIME = 1
EMP_RATE_PER_HOUR = 20


class EmployeeWageBuilder:
    def __init__(self):
        self.check_attendence = 0

    check_attendence = random.randint(0, 1)
    if check_attendence == IS_FULL_TIME:
        emp_hrs = 8
    else:
        emp_hrs = 0
    emp_wage = emp_hrs * EMP_RATE_PER_HOUR
    print("Daily Employee Wage is:", emp_wage)


