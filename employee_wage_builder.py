import random
from employee_wage_interface import EmpWageMethods

wage_list = []


class EmployeeWageBuilder(EmpWageMethods):
    def __init__(self, company_name, wage_rate_per_hour, no_of_working_days, max_hrs_in_month, emp_hrs=0, emp_wage=0,
                 total_emp_wage=0, total_working_days=0, total_working_hours=0):
        self.emp_hrs = emp_hrs
        self.emp_wage = emp_wage
        self.total_emp_wage = total_emp_wage
        self.total_working_days = total_working_days
        self.total_working_hours = total_working_hours
        self.COMPANY_NAME = company_name
        self.WAGE_RATE_PER_HOUR = wage_rate_per_hour
        self.NO_WORKING_DAYS = no_of_working_days
        self.MAX_HRS_IN_MONTH = max_hrs_in_month

    def total_employee_wage(self):
        while self.total_working_hours <= self.MAX_HRS_IN_MONTH and self.total_working_days <= self.NO_WORKING_DAYS:
            self.total_working_days = self.total_working_days + 1
            type_of_employee = random.randint(1, 3)
            self.emp_hrs = self.get_work_hours(type_of_employee)
            self.total_working_hours = self.total_working_hours + self.emp_hrs
            self.emp_wage = self.emp_hrs * self.WAGE_RATE_PER_HOUR
            self.total_emp_wage = self.total_emp_wage + self.emp_wage
            list_vales = f"{self.COMPANY_NAME, self.emp_wage, self.total_emp_wage}"
        wage_list.append(list_vales)
        print(wage_list)
        print("Total Conditional Wage:", self.total_emp_wage)

    def get_work_hours(self, value):
        switcher = {
            1: 8, 2: 4, 3: 0
        }
        return switcher.get(value, "hi")

    def print_list(self, list_emp_wage):
        print("Printing Complete List")
        for per in list_emp_wage:
            print(per)

    def __str__(self):
        return f"{self.COMPANY_NAME, self.emp_wage, self.total_emp_wage}"
