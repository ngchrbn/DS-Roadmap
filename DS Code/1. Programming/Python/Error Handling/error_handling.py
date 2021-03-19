"""
a. Raising an Exception:
    ==> We can use 'raise' to throw an exception
        if a condition occurs

b. AssertionError exception:
    ==> Instead of waiting for a program to crash midway,
        you can also start by making an assertion.
        We assert that a certain condition is met. If the
        condition is True, then the program continues,
        If the condion is False, you can have the program
        throw an AssertionError exception.

c. try and except block:
    ==> Synthax:
            try:
                Run this code
            except:
                Execute this code when there is an exception

d. else clause:
            try:
                Run this code
            except:
                Execute this code when there is an exception
            else:
                No exceptions? Run this code.

e. finally clause:
            try:
                Run this code
            except:
                Execute this code when there is an exception
            else:
                No exceptions? Run this code.
            finally:
                ALways run this code.

"""


import sys

def linux_interaction():
    assert ('Linux'.lower() in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
    

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')