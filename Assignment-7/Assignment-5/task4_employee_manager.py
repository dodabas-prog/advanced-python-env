class employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


class manager(employee):
    def __init__(self, name, salary, bonus_percent):
        super().__init__(name, salary)
        self.bonus_percent = bonus_percent

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.get_salary() * (self.bonus_percent / 100)


def print_employees(emp_list):
    for e in emp_list:
        print(f"{e.get_role()} | salary: {e.get_salary()}")


e1 = employee("Amina", 200000)
m1 = manager("Karima", 300000, 10)

employees = [e1, m1]
print_employees(employees)
print("Manager bonus:", m1.get_bonus())