class Human:
    def __init__(self, name):
        self.name = name
import random


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers != []:
            print(f'Name of {self.brand} passengers')
            for name in self.passengers:
                print(name.name)
        else:
            print(f'No passengers in {self.brand}')

nick = Human('Nick')
kate = Human('Kate')
car = Auto('Mercedess')

car.add_passengers(nick)
car.add_passengers(kate)

car.print_passengers_names()



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
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.glandess -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manege):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manege == 'fuel'
            else:
                self.to_repair()
                return
        if manege == ('fuel'):
            print('I bought fuel!')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food!')
            self.money -= 50
            self.home.food += 50
        elif manege == 'delicacies':
            print('I happy! Delicacies')
            self.glandess += 10
            self.satiety += 2
            self.money -= 15

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")


    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def clean_home(self):
        self.glandess -= 5
        self.home.mess = 0
    def chill(self):
        self.glandess += 10
        self.home.mess += 5
    def is_alive(self):
        if self.glandess <= 0:
            print('Depression..')
            return False
        if self.satiety <0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in the house!')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f'I bought a car {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, going to get a job {self.job.job}"
                  f"with salary {self.job.salary}")

        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("I'll go eat!")
            self.eat()
        elif self.glandess < 20:
            if self.home.mess > 15:
                self.home.clean()
            else:
                print("Tim's chill")
                self.chill()
        elif self.money < 0:
            print('Start working!')
            self.work()
        elif self.car.strenght < 15:
            print("I need to repair my car!")
            self.to_repair()
        if dice == 1:
            print("Let's chill!")
            self.chill()
        elif dice == 2:
            print('Start working!')
            self.work()
        elif dice == 3:
            print('Cleaning time!')
            self.clean_home()
        elif dice == 4:
            print("Time for teats")
            self.shopping(manege='delicacies')



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



nick = Human(name='Nick')
for day in range(1, 365):
    if nick.live(day) == False:
        break