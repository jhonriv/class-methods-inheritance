from Person import Person
from Dog import Dog
from Employee import Employee
from Rectangule import Rectangule
from Automovil import Automovil

Person1 = Person("John", 36)
Person2 = Person("Jane", 25)
Person1.print_person()
Person2.print_person()

Dog1 = Dog("Fido", "Labrador")
Dog1.print_dog()

Employees = []
Employees.append(Employee("John", 1000, "IT"))
Employees.append(Employee("Jane", 3000, "HR"))
Employees.append(Employee("Jack", 3000, "Finance"))
def employees_highest_salary(employees):
    highest_salary = max(employees, key=lambda employee: employee.salary).salary
    employees = list(filter(lambda employee: employee.salary == highest_salary, employees))
    print(f"The highest salary is {highest_salary}, and the employees with the highest salary are:")
    for employee in employees:
        print(employee.name)
employees_highest_salary(Employees)


Rectangule1 = Rectangule(10, 20)
print(Rectangule1.get_area())
print(Rectangule1.get_perimeter())


Automovil1 = Automovil("Toyota", "Corolla", "Red")
Automovil1.auto_info()