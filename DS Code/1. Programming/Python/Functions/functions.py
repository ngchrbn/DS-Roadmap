"""
Functions in Python are first-class objects. 
Programming language theorists define a 
"first-class object" as a program entity that can be:

- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a function
- Returned as the result of a function


Synthax ==> def function_name(arg1, arg2,...,argN):
                --- statements here ---


"""

# Declaring and Calling a Function

def sayHello(name):
    print('Hello', name)

# Calling a function
sayHello('Guy')

# Function without parameters
def generate_full_name():
    first_name = 'Guy'
    last_name = 'Cherubin'
    print(first_name, last_name)

generate_full_name()

# Function returning a Value(s)
def get_full_name():
    first_name = 'Guy'
    last_name = 'Cherubin'
    return first_name + ' ' + last_name

get_full_name()

# Function with parameters
def print_name(first_name, last_name):
    return f'{first_name} {last_name}'

print(print_name('Guy', 'Cherubin'))

# Function with default value(s)
def print_name1(first_name='', last_name=''):
    return f'{first_name} {last_name}'

print_name1()

# Arbitrary number of arguments

def get_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(get_sum(1, 2, 3, 4))
print(get_sum(1, 3))

# Function as parameter
def square_number(n):
    return n * n

def square_n(fun, n):
    return fun(n)

print(square_n(square_number, 6))


# Function as a return value
def add_number(n):
    return n + n

def do_something(n, what=''):
    if what == 'square':
        return square_number(n)
    elif what == 'add':
        return add_number(n)
    else:
        return 'Nothing to do'

print(do_something(5, 'square'))
print(do_something(6, 'add'))


# Full example

# Number of days per month.
# First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    elif month == 2 and is_leap(year):
        return 29

    else:
        return month_days[month]

print("The number of days are:", days_in_month(2021, 2))