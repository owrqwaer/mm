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
#import random
#from random import random
import random


class Student:
    # print("Hi")
    #group = 'C2013'

    def __init__(self, name=None):
        # print(id(self))
       # self.height = 150
        #self.weight = 60
        #self.age = age
        self.name = name
        self.alive = True
        self.gladness = 50
        self.progress = 0
    def to_study(self):
        print('Time to study!')
        self.progress += 0.12
        self.gladness -= 5
    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1
    def to_sleep(self):
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print('Passed externally...')
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
    def live(self, day):
        day = "Day " + str(day) + "of " + self.name +  " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


    #def printer(self):
        #print(self.weight)
        # print('I am alive!')

    #def grow(self, height=10):
        #self.height += height

    #def __str__(self):
        #return f'I am Student. My name is {self.name} ' \
               #f'"f"and i am {self.age} old'


# first_student = Student()
# print(id(first_student))
# print(first_student.weight)
# print(first_student.height)
#nick = Student(15, "Nick", 200)
# nick.height = 170
# nick.weight = 85
# print(nick.height)
# print(nick.weight)
#kate = Student(16, "Kate", 150)
#print(nick.age)
#print(kate.age)
#print(nick.height)
#print(kate.height)
#print(nick.group, kate.group)
#nick.printer()
#kate.grow()
#print(kate.height)
#kate.grow(25)
