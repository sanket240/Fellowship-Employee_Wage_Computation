from employee_wage_builder import EmployeeWageBuilder
if __name__ == '__main__':
    i = int(input('Enter total number of companies:'))
    for i in range(0, i):
        WAGE_RATE = int(input("Enter Wage Rate:"))
        MAX_HRS = int(input("Enter Max hours:"))
        MAX_WORKING_DAYS = int(input("Enter max working days:"))
        emp = EmployeeWageBuilder(WAGE_RATE, MAX_HRS, MAX_WORKING_DAYS)
        emp.total_employee_wage()


