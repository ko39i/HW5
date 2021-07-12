1.


class Laptop:
    def __init__(self):
        battery = Battery('This is charge for battery')
        self.battery = [battery]


class Battery:
    def __init__(self, charge):
        self.charge = charge


laptop = Laptop()

2.


class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring


class GuitarString:
    def __init__(self):
        pass


guitarstring = GuitarString()
guitar = Guitar(guitarstring)

3.
import datetime

class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return print(x + y + z)

calc = Calc()
calc.add_nums(3, 4, 5)

4.
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta ({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


print(Pasta.carbonara())
print(Pasta.bolognaise())

5
class Concert:
    def __init__(self, max_visitors_num):
        self.max_visitors_num = max_visitors_num

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value if value < self.max_visitors_num else self.max_visitors_num



concert = Concert(50)
concert.visitors_count = 1000
print(concert.visitors_count)
6
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    key = int
    name = str
    phone_number = str
    address = str
    email = str
    birthday = str
    age = int
7
from collections import namedtuple

AddressBook = namedtuple('AddressBook', ['key', 'name', 'phone_number0', 'address', 'email', 'birthday', 'age'])

8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook: {self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}"

    def __repr__(self):
        return f"AddressBook('{self.key}, {self.name}, {self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}')"

addressbook = AddressBook('2','Jon', '4542', '5 Stone Street, Apt. 2A, Jacksonville, FL 39404', 'jon32@mailcom', '12/02/2000', '21')

print(addressbook)
9

class Person:
    name = "John"
    age = 36
    country = "USA"


person = Person
setattr(person, "age", 23)
print(person.age)

10
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student
setattr(student, "email", "student@mail.com")
setattr(student, "student_email", "student@mail.com")
print(getattr(student, "student_email",))

11
class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert(self):
        self._convert = (self._temperature * 1.8) + 32
        return self._convert


fahrenheit = Celsius()
print(fahrenheit.convert)