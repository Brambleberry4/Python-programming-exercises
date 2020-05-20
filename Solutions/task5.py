"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class MyClass(object):

    def __init__(self):
        self.s = ''

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


test1 = MyClass()
test1.getString()
test1.printString()

test2 = MyClass()
test2.getString()
test2.printString()