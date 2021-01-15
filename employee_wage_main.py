from employee_wage_builder import EmployeeWageBuilder
if __name__ == '__main__':
    emp_wage_list = []
    emp_obj = []
    no_of_companies = int(input("Enter number of companies:"))
    for i in range(0, no_of_companies):
        company_name = input("Enter Company Name:")
        wage_rate = int(input("Enter Wage rate:"))
        no_of_working_days = int(input("Enter number of working days: "))
        max_hrs = int(input("Enter Max hours:"))
        emp_obj = EmployeeWageBuilder(company_name, wage_rate, no_of_working_days, max_hrs)
        emp_obj.total_employee_wage()
        emp_wage_list.append(emp_obj)
    emp_obj.print_list(emp_wage_list)

