import random
IS_FULL_TIME = 1
IS_PART_TIME = 2
EMP_RATE_PER_HOUR = 20
PART_TIME_RATE_PER_HOUR = 8
NO_WORKING_DAYS = 20
MAX_HRS_IN_MONTH=100



class EmployeeWageBuilder:
    def __init__(self, check_attendence=0, emp_hrs=0, emp_wage=0, total_emp_wage=0, total_working_days=0,total_working_hours=0):
        self.check_attendence = check_attendence
        self.emp_hrs = emp_hrs
        self.emp_wage = emp_wage
        self.total_emp_wage = total_emp_wage
        self.total_working_days = total_working_days
        self.total_working_hours = total_working_hours

    def total_employee_wage(self):
        while self.total_working_hours <= MAX_HRS_IN_MONTH and self.total_working_days <= NO_WORKING_DAYS:
            self.total_working_days = self.total_working_days + 1
            type_of_employee = random.randint(1, 3)
            self.emp_hrs = self.get_work_hours(type_of_employee)
            self.total_working_hours = self.total_working_hours + self.emp_hrs
            self.emp_wage = self.emp_hrs * EMP_RATE_PER_HOUR
            self.total_emp_wage = self.total_emp_wage + self.emp_wage
        print("Total Conditional Wage:", self.total_emp_wage)

    def get_work_hours(self, value):
        switcher = {
            1: 8, 2: 4, 3: 0
        }
        return switcher.get(value, "hi")



