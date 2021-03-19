"""
-----------------------------MAP()------------------------------

map(function, iterable, ...) returns an iterator that applies
function to every item of iterable, yielding the results.
If additional iterable arguments are passed, function must take
that many arguments and is applied to the items from all
iterables in parallel. With multiple iterables, the iterator
stops when the shortest iterable is exhausted.

Returns an iterator.
"""

# Example 1
print(list(map(lambda *a: a, range(3))))

# Example 2
print(list(map(lambda *a: a, range(3), 'abc')))

# Example 3
print(list(map(lambda *a: a, (1, 2, 3, 4), 'abc')))

# Full Example

students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(student):
    # Create a 2-tuple (sum of credits, student) from student dict
    return (sum(student['credits'].values()), student)

def undecorate(decorated_student):
    # Discard sum of credits, return original student dict
    return decorated_student[1]

def print_students(students):
    for student in students:
        print(student)

students = sorted(map(decorate, students), reverse=True)
print("\nStudents after sorting them by their sum", print_students(students))
students = list(map(undecorate, students))
print("\nStudents' Scores", students)




"""
-----------------------------FILTER()------------------------------

filter(function, iterable) construct an iterator from those elements
of iterable for which function returns True.
Iterable may be either a sequence, a container which supports
iteration or an iterator. 
If function is None, the identity function is assumed, that is,
all elements of iterable that are false are removed.

Returns an iterator.
"""

# Example
test = [2, 5, 8, 0, 0, 1, 0]
print(list(filter(None, test)))
print(list(filter(lambda x: x, test)))
print(list(filter(lambda x: x > 4, test)))  # keep only items > 4



"""
-----------------------------ZIP()------------------------------

zip(*iterables) returns an iterator of tuples, where the i-th
tuple contains the i-th element from each of the argument sequences
or iterables. The iterator stops when the shortest input iterable
is exhausted.
With a single iterable argument, it returns an iterator of 1-tuples.
With no arguments, it returns an empty iterator.

Returns an iterator.
"""

# Example

grades = [18, 23, 30, 27, 15, 9, 22]
avgs = [22, 21, 29, 24, 18, 18, 24]

print(list(zip(avgs, grades)))

a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]
maxs = map(lambda n: max(*n), zip(a, b, c))

print(list(maxs))