# class parent_class:
#     print("I am a Parent Class")

#     def m1():
#         print("I am a method")


# p = parent_class
# p.m1()


# class parent_class2:
#     def __init__(self, Employee_name, Salary):
#         self.Employee_name = input("Enter the Name:")
#         self.Salary = input("Enter the Salary:")

#     def display(self):
#         print("I am a Method")
#         print(self.Employee_name)
#         print(self.Salary)


# p2 = parent_class2("a", 8000)
# p2.display()


# class child_class(parent_class2):
#     def __init__(self, Employee_name, Salary, id):
#         super().__init__(Employee_name, Salary)
#         self.id = int(input("Enter Id:"))

#     def show(self):
#         print("Welcome")


# c = child_class("a", 2, 3)
# c.display()
# c.show()


# Overriding Method
# class p_class:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def getname(self):
#         return self.name

#     def getsalary(self):
#         return self.salary


# p = p_class("Priyansh", 50000)


# class c_class(p_class):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus

#     def getname(self):
#         return self.bonus + self.salary


# c = c_class("Rekha", 20000, 500)
# print(p.getname(), p.getsalary())
# print(c.getname())


# overloading
# class c1:
#     def add(self, a, b, c=0):
#         return a + b + c


# ob = c1()
# print(ob.add(10, 20))
# print(ob.add(10, 20, 30))


# Dunder method
# class cc:
#     def __len__(self, string):
#         self.string = string
#         return len(self.l1)


# ob = cc()
# print(len("hello"))

# list comprehension
# s = [i**2 for i in range(1, 51) if i % 2 == 0]
# print(s)


# words = ["hello", "world", "Python", "list"]
# lengths = [len(i) for i in words]
# print(lengths)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [n for i in matrix for n in i]
# print(result)


# list = [i for i in range(11) if i % 2 == 0]
# print(list)

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)


# Generator
# def fun(n):
#     for i in range(n):
#         yield i


# a = fun(5)
# print(next(a))
# print(next(a))
# print("helo")
# for value in a:
#     print(value)

# sort the value by  second value
# data = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("David", 20)]
# result = sorted(data, key=lambda x: x[1])
# print(result)


# generator expressions that generates even numbers up to 100.
# def even_num(n):
#     for i in range(n + 1):
#         if i % 2 == 0:
#             yield i


# a = even_num(100)
# print(next(a))
# print(next(a))
# print(next(a))
