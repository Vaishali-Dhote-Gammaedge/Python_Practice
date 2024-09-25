# def my_decor(func):
#     def wrapper():
#         print("This is First line")
#         func()
#         print("This is Second line")

#     return wrapper


# @my_decor
# def main_fun():
#     print("This is original Function")


# main_fun()


# def my_decor2(func):
#     def wrap_fun(a, b):
#         func(a, b)
#         print("Decorators Done")

#     return wrap_fun


# @my_decor2
# def divide(a, b):
#     print(f"Division of {a} and {b} is:", a / b)


# divide(10, 5)
