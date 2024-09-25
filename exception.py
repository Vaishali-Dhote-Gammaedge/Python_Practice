#  Error
# a = 2000
# if(a > 1000)
# print("Valid Number")


# exception
# a = 9
# try:
#     b = a / 0
# except ZeroDivisionError:
#     print("Can't Divide")


# a = [1, 2, 3]
# try:
#     print("Second element = %d" % (a[1]))
#     print("Fourth element = %d" % (a[3]))
# except:
#     print("Not Available")


# def fun(a):
#     if a < 10:
#         b = a / (a - 8)
#     print("Value of b:", b)
# try:
#     # fun(8)
#     fun(5)
# except ZeroDivisionError:
#     print("Division Error Occurred")


# else clause
# def fun2(x, y):
#     try:
#         z = (x + y) / (x - y)
#     except ZeroDivisionError:
#         print("Division Error Occurred")
#     else:
#         print("value of Z:", z)


# # fun2(5, 8)
# fun2(5, 5)


# finally keyword
# a = 9
# try:
#     b = a / 0
# except ZeroDivisionError:
#     print("Can't Divide")
# finally:
#     print("Always Excecute")


# Raising Exception
# try:
#     raise NameError("Hello")
# except NameError:
#     print("Error Occurred")
#     raise
