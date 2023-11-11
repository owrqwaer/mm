#class Parent:
#    age = 45

#class Child:
#    age = 15

#class Grandparent:
#    height = 170
#   satiety = 100
#   age = 60

#class Parent(Grandparent):
 #   height = 90
  #  def __init__(self):
   #     print(self.height)
    #    print(self.satiety)
     #   print(self.age)

#nick = Child()
#print(nick.age)

class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"

    def __init__(self):
        self.world == "world"
        self._world = "_world"
        self.__world = "__world"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_print()