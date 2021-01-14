from employee_wage_builder import EmployeeWageBuilder
if __name__ == '__main__':
    tata = EmployeeWageBuilder("Tata", 20, 20, 100)
    tata.total_employee_wage()
    print(tata)
    reliance = EmployeeWageBuilder("Reliance", 30, 30, 180)
    reliance.total_employee_wage()
    print(reliance)
