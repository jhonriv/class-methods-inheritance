class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def get_employee(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "department": self.department
        }