class Panda:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def sleep(self,hours=None):
        self.hours=hours
        if self.hours==None:
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
        elif self.hours>=3 and self.hours<=5:
            return f"{self.name} sleeps {self.hours} hours daily and should have Mixed Veggies"
        elif self.hours>=6 and self.hours<=8:
            return  f"{self.name} sleeps {self.hours} hours daily and should have Eggplant & Tofu"
        elif self.hours>=9 and self.hours<=11:
            return f"{self.name} sleeps {self.hours} hours daily and should have Broccoli Chicken"


panda1= Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female", 3)
panda3 = Panda("Ming Ming", "Female", 8)

print("{} is a {} Panda Bear who is {} years old".format(panda1.name, panda1.gender, panda1.age))

print("{} is a {} Panda Bear who is {} years old".format(panda2.name, panda2.gender, panda2.age))

print("{} is a {} Panda Bear who is {} years old".format(panda3.name, panda3.gender, panda3.age))


print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())

