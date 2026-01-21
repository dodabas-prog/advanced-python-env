class person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

    def introduce(self):
        return f"Hi, I am {self.name}. I am {self.__age} years old."


class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Hi, I am {self.name}. I am {self.get_age()} years old. My id is {self.student_id}."


p = person("Amina", 18)
s = student("Karima", 19, "257032")

people = [p, s]

for x in people:
    print(x.introduce())