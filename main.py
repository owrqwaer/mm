#class Haman:
 #   def __init__(self, name):
     #   self.name = name
import random


#class Auto:
 #   def __init__(self, brand):
  #      self.brand = brand
   #     self.passengers = []

    #def add_passengers(self, human):
     #   self.passengers.append(human)

    #def print_passengers_names(self):
     #   if self.passengers != []
      #      print(f'Name of {self.brand} passengers')
       #     for name in self.passengers:
        #        print(name.name)
        #else:
         #   print(f'No passengers in {self.brand}')

#nick = Human('Nick')
#kate = Human('Kate')
#car = Auto('Mercedess')

#car.add_passengers(nick)
#car.add_passengers(kate)

#car.print_passengers_names()



class Human:

    def __init__(self, name="Human", job=None, car=None, home=None  ):
        self.car = car
        self.name = name
        self.job = job
        self.money = 100
        self.glandess = 50
        self.satiety = 50
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shoping("food")



class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The cat cannot move!")
            return False


class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 60, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 15},
}




brands_of_car = {
        "BMW":{"fuel": 100, "strength": 100, "consumption": 6},
       "Lada":{"fuel": 50, "strength": 40, "consumption": 10},
       "Volvo":{"fuel": 80, "strength": 150, "consumption": 8},
       "Ferrari":{"fuel": 80, "strength": 120, "consumption": 14}}

h = Human