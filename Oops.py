# 1. Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
# import math


# class circle:
#     def __init__(self, raidus):
#         self.raidus = raidus

#     def c_area(self):
#         return math.pi * self.raidus**2

#     def c_perimeter(self):
#         return 2 * math.pi * self.raidus


# cc = circle(6)
# print(f"Area of Circle is:{round(cc.c_area(), 2)}")
# print(f"Perimeter of Circle is:{round(cc.c_perimeter(), 2)}")


# Write a Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
# import datetime
# from datetime import date


# class person:
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth

#     def person_age(self):
#         y1 = datetime.date.today()
#         age = y1.year - self.date_of_birth.year
#         return age


# p = person("A", "I", date(2003, 4, 5))
# print(f"Age of is:{p.person_age()}")


#  Write a Python program to create a Vehicle class with max_speed
# and mileage instance attributes.
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = input("Enter Max_speed of vehicle:")
#         self.mileage = input("Enter the mileage of vehicle:")

#     def show(self):
#         print(
#             "vehicle's max_speed ", self.max_speed, " and mileage",
#           self.mileage
#         )


# v = Vehicle(240, 18)
# v.show()


# Create a child class Bus that will inherit all of the variables and
# methods of the Vehicle class
# class bus(Vehicle):
#     def __init__(self, max_speed, mileage, seat_capacity=50):
#         super().__init__(max_speed, mileage)
#         self.seat_capacity = int(input("Enter the seating capacity:"))

#     def seating_capacity(self):
#         print("Capacity of vehicle:", self.seat_capacity)


# b = bus(210, 35, 5)
# b.show()
# b.seating_capacity()


# multiple inhertiance
# class person:
#     def person_info(self, name, age):
#         print("Name:", name, "age:", age)


# p = person()
# p.person_info("Tanu", 21)


# class company:
#     def company_info(self, company_name, location):
#         print("Company_name:", company_name, "Location:", location)


# c = company()
# c.company_info("Gammaedge", "Near Khandwa Naka")


# class employee(person, company):
#     def employee_info(self, salary, skill):
#         print("Salary:", salary, "skill:", skill)


# e = employee()
# e.employee_info(25000, "python")
# e.person_info("Chirag", 22)
# e.company_info("Gammaedge", "Indore")


# multilevel inheritance
# class vehicle:
#     def show(self):
#         print("This is parent class...")


# class car(vehicle):
#     def display(self):
#         print("This is child1 class...")


# class sportcar(car):
#     def info(self):
#         print("This is child2 class...")


# s = sportcar()
# s.show()
# s.display()
# s.info()


# Hierarchical Inheritance
# class vehicle:
#     def info(self):
#         print("This is parent class")


# class car(vehicle):
#     def show(self):
#         print("This is child1 class...")


# c = car()
# c.info()
# c.show()


# class truck(vehicle):
#     def display(self):
#         print("This is child2 class")


# t = truck()
# t.display()
# t.info()


# class animal:
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         pass


# class dog(animal):
#     def make_sound(self):
#         return "bark"


# class cat(animal):
#     def make_sound(self):
#         return "meow"


# d = dog("sheru")
# print(d.name, d.make_sound())

# c = cat("Billi")
# print(c.name, c.make_sound())
