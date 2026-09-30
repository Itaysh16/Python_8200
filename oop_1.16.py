class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof Woof! and it is {self.age} year old")
dog1 = Dog("Ori", 16)
dog2 = Dog("Avishag", 18)

dog1.bark()
dog2.bark()
print()
print()



from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius**2)

    def __str__(self):
        return f"Circle (radius={self.radius}, area={self.area():.2f})"

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width

    def __str__(self):
        return f"Rectangle ({self.width}x{self.height}, area={self.area():.2f})"

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5*self.height*self.base

    def __str__(self):
        return f"Triangle (base={self.base}, height={self.height}, area={self.area():.2f})"

shapes = [
    Rectangle(3, 5),
    Circle(2),
    Triangle(10, 2),
]

shapes.sort()
print("--------Shapes sorted by area--------")
for shape in shapes:
    print(shape)
print()
print()


class BankAccount:

    def __init__(self, owner, initial_balnce):
        self.owner = owner
        self._balance = initial_balnce

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        else:
            self._balance = value

    def __str__(self):
        return f"Account[Owner: {self.owner}, Balance: {self.balance}]"

account = BankAccount("Itay", 1000000)
print(f"{account} Dollars")
account2 = BankAccount("Ori", 1000)

account3 = BankAccount("Evyatar", 2000)

account.balance = 1500
print(f"New balance: {account.balance} Dollars")

try:
    account.balance = -500
except ValueError as error:
    print(f"Blocked invalid balance: {error}")
