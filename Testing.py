# from doctest import testmod

# def fact(n):
#     """This function returns the factorail of any number
#     >>> fact(2)
#     2
#     >>> fact(3)
#     6
#     >>> fact(4)
#     24
#     >>> fact(5)
#     120
#     """
#     facto = 1
#     for i in range(1, n + 1):
#         facto = facto * i
#     print(facto)


# if __name__ == "__main__":
#     testmod(name="fact()", verbose=True)


# def fun(n):
#     """This Function tells the type of number
#     >>> fun(3)
#     'Positive Number'
#     >>> fun(0)
#     'Zero'
#     >>> fun(-8)
#     'Negative Number'
#     """
#     if n > 0:
#         return "Positive Number"
#     elif n == 0:
#         return "Zero"
#     else:
#         return "Negative Number"


# if __name__ == "__main__":
#     testmod(verbose=True)


# def add(l1):
#     """
#     This increase the element of list by 2
#     >>> add([1,2,3])
#     [3, 4, 5]
#     >>> add([1,1,1])
#     [3, 3, 3]
#     """
#     return [i + 2 for i in l1]


# if __name__ == "__main__":
#     testmod(verbose=True)

# import unittest


# def add(a, b):
#     return a + b


# class testadd(unittest.TestCase):
#     def test_add_positive(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative(self):
#         self.assertEqual(add(-5, -9), -14)


# if __name__ == "__main__":
#     unittest.main()


# class test_string(unittest.TestCase):
#     def test_s1_split(self):
#         s1 = "Hello Gammaedge 2024"
#         self.assertEqual(s1.split(), ["Hello", "Gammaedge", "2024"])

#     def test_string_repeat(self):
#         self.assertEqual("Hello" * 4, "HelloHelloHelloHello")

#     def test_string_upper(self):
#         self.assertEqual("Gammaedge".upper(), "GAMMAEDGE")


# if __name__ == "__main__":
#     unittest.main()


# import pytest

# def add(n):
#     return n + 6


# def test_add():
#     assert add(5) == 11


# def test_1():
#     a = 3
#     b = 2 + 1
#     assert a == b


# def test_2():
#     a = 7
#     b = 2
#     assert (a - b) == 5


# nose testing
# def test_fun():
#     assert 2 * 3 == 6


# import unittest


# class MyTestCase(unittest.TestCase):
#     def setUp(self):
#         # This method is called before each test
#         self.test_data = [1, 2, 3]

#     def tearDown(self):
#         # This method is called after each test
#         self.test_data = None

#     def test_sum(self):
#         # Using the fixture set up in setUp()
#         self.assertEqual(sum(self.test_data), 6)

#     def test_length(self):
#         self.assertEqual(len(self.test_data), 3)


# if __name__ == "__main__":
#     unittest.main()

# import pytest


# @pytest.fixture
# def fun():
#     data = [1, 2, 3]
#     yield data


# def test_sumfun(fun):
#     assert sum(fun) == 6


# def test_lenfun(fun):
#     assert len(fun) == 3

# parameterized test in pytest

# import pytest


# def square(n):
#     return n * n


# @pytest.mark.parametrize(
#     "input_value, Expected_value", [(2, 4), (3, 9), (4, 16), (5, 25)]
# )
# def test_square(input_value, Expected_value):
#     assert square(input_value) == Expected_value

import unittest


def divide(a, b):
    if b == 0:
        raise ValueError("Can't Divide by Zero")


class test_divide(unittest.TestCase):
    def test_division(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Can't Divide by Zero")


if __name__ == "__main__":
    unittest.main()
