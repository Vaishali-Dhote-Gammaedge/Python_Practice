# import re

# txt = "Welcome to Gammaedge 2024"
# result = re.findall("\d", txt)
# print(result)

# txt = "Welcome to Gammaedge"
# result = re.findall("^W.*e$", txt)
# if result:
#     print("Yes")
# else:
#     print("NO")


# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#     print("YES! We have a match!")
# else:
#     print("No match")


# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs.")
#         func()  # This calls the original function
#         print("After the function runs.")

#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")


# say_hello()


# def deco(fun):
#     def wrap(a, b):
#         print("Before Running")
#         fun(a, b)
#         print("After Running")

#     return wrap


# @deco
# def divide(a, b):
#     print(a / b)


# divide(2, 5)

# iterators
fruits = ["apple", "banana", "cherry"]


fruit_iterator = iter(fruits)

print(next(fruit_iterator))
print(next(fruit_iterator))
print(next(fruit_iterator))
