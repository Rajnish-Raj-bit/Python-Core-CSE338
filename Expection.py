class TooYoungError(Exception):
    def __init__(self, message):
        self.mess = message
    def __str__(self):
        return self.mess

class TooOldError(Exception):
    def __init__(self, message):
        self.mess = message
    def __str__(self):
        return self.mess

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_age(self , age):
        if age < 18:
            raise TooYoungError("You are too young")
        elif age > 65:
            raise TooOldError("You are too old")
        else:
            self.age = age


p1 = Person("Rajnish" , 20)
ask_age = int(input("Enter your age: "))
try:
    p1.set_age(ask_age)

except TooOldError as obj:
    print(obj)

except TooYoungError as obj:
    print(obj)