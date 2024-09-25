print("Hello World")

# data types in python
# 1. integer
# 2. float
# 3. boolean
# 4. string

# type conversion in python
x = 12.35
y = int(x)
print(type(y))

x = 12
y = float(x)
print(type(y))

x = 12
y = str(x)
print(type(y))

x = 12
y = bool(x)
print(type(y))

# # conditional statement in python
a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))
c = int(input("Enter a NUmber:"))

if a > b:
    if a > c:
        print(a, "is Greater")
    else:
        print(c, "is Greater")
else:
    if b > c:
        print(b, "is Greater")
    else:
        print(c, "is Greater")


# Example of default parameters
def fact(num=2):
    facto = 1
    for i in range(1, num + 1):
        facto = facto * i
    print(f" The Factorial of {num} is {facto}")


# fact(6)


# list comprehension
l1 = [x**2 for x in range(11)]
print(l1)


# adding and removing elements from set
s1 = {"Employee_1", "Employee_2", "Employee_3", "Employee_4"}
s1.remove("Employee_3")
print(s1)

s1.add("Employee_3")
print(s1)


# Dictionary
d1 = {
    "Name": ["Rohit", "kapil", "Mohan", "Raj"],
    "Salary": [20000, 30000, 40000, 50000],
}
print(d1)
print(len(d1))
print(d1.keys)
print(d1.values)


# # Message based on input type
n = input("Enter your name:")
print(f"Welcome to Gammaedge {n} !!!")
