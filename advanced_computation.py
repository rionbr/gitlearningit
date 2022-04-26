# -*- coding: utf-8 -*-
"""
Git Learning Git
===================

The main source code that can be altered in multiple locations.
Try branching, modifying a particular function,
creating a new class or expanding it, and then issuing a pull request.
Remember to always document the method or class you define.
"""


class AdvancedComputation(object):

    def __init__(self):
        self.value = 0  # the variable state of the class
        self.counter = 0  # internal counter of how many times this class has been called.

    ## TODO new methods

    def set_value(self, value):
        self.value = value
        return True

    def get_value(self):
        return self.value

    def __increase_counter(self):
        self.counter += 1


if __name__ == '__main__':
    # Debug
    a = 1
    b = 2
    # instanciate class
    BC = AdvancedComputation()
    print(BC)

    print("counter:", BC.counter)
