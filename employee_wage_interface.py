import abc


class EmpWageMethods(abc.ABC):
    @abc.abstractmethod
    def total_employee_wage(self):
        pass

    @abc.abstractmethod
    def get_work_hours(self, value):
        pass

    @abc.abstractmethod
    def print_list(self, list_emp_wage):
        pass
