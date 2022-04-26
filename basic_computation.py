# -*- coding: utf-8 -*-
"""
Git Learning Git
===================

The main source code that can be altered in multiple locations.
Try branching, modifying a particular function,
creating a new class or expanding it, and then issuing a pull request.
Remember to always document the method or class you define.
"""


class BasicComputation(object):

    def __init__(self):
        self.value = 0  # the variable state of the class
        self.counter = 0  # internal counter of how many times this class has been called.

    def sum_two_variables(self, a, b):
        """ This function sums two variables

        Args:
            a (int): first variable
            b (int): second variable

        Returns:
            int: summed variable
        """
        c = a + b
        self.__increase_counter()
        return c

    def multiply_two_variables(self, a, b):
        """ This function multiples two variables"""
        c = a * b
        self.__increase_counter()
        return c

    def set_value(self, value):
        self.value = value
        return True

    def get_value(self):
        return self.value

    def __increase_counter(self):
        self.counter += 1

    def __decrease_counter(self):
        self.counter -= 1

if __name__ == '__main__':
    # Debug
    a = 1
    b = 2
    # instanciate class
    BC = BasicComputation()
    print(BC)

    print("fist sum:", BC.sum_two_variables(a, b))
    print("counter:", BC.counter)
    print("second sum:", BC.sum_two_variables(a, b))
    print("counter:", BC.counter)
