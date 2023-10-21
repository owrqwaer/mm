# class Forest:
#    height = 100
#    weight = 5
#   age = 25
#    color_list = 'green'
#    breed = 'oak'
#
#    def __init__(self):
#        print(Forest.height)
#        print(Forest.age)
#
# tree1 = Forest()
# print(tree1)

class Student:
    # print("Hi")
    group = 'C2013'

    def __init__(self, age, name=None, height=160):
        # print(id(self))
        self.height = 150
        self.weight = 60
        self.age = age
        self.name = name

    def printer(self):
        print(self.weight)
        # print('I am alive!')

    def grow(self, height=10):
        self.height += height

    def __str__(self):
        return f'I am Student. My name is {self.name} ' \
               f'"f"and i am {self.age} old'


# first_student = Student()
# print(id(first_student))
# print(first_student.weight)
# print(first_student.height)
nick = Student(15, "Nick", 200)
# nick.height = 170
# nick.weight = 85
# print(nick.height)
# print(nick.weight)
kate = Student(16, "Kate", 150)
print(nick.age)
print(kate.age)
print(nick.height)
print(kate.height)
print(nick.group, kate.group)
nick.printer()
kate.grow()
print(kate.height)
kate.grow(25)
