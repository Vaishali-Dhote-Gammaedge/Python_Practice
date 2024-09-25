# d1 = {"Name": ["a", "b", "c", "d"], "Salary": [1000, 2000, 3000, 4000]}
# print(d1)
# # print(d1.keys())
# # print(d1.values())

# for keys,values in d1.items():
#     print(keys,values)


# l1 = [1, 2, 3, "Rohit", "Piyush"]
# print(l1[2])

# t1 = (1, 2, 3, "A", "B")
# print(t1[2])

a = [1, 2, 3]

try:
    print("Second element = %d" % (a[1]))

    print("Fourth element = %d" % (a[3]))
except:
    print("An error occurred")
