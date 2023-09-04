from hw4 import Shakhmin,Rustam,Gulina,Mirlan



class Bekbolot(Shakhmin,Rustam,Gulina,Mirlan):
    def __init__(self, name, age):
        Shakhmin.__init__(self, name)
        Rustam.__init__(self, age)


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value

russtam = Bekbolot('beka', 23)
print(russtam.name, russtam._age)