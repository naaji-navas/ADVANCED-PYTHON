"""
This imports the module sys and sets the recursion limit to 10000
"""
from functools import reduce, cache

import sys
# create a function which takes two arguments and returns the sum of the two
# arguments
sys.setrecursionlimit(10000)

""""
a function which takes two arguments and returns the sum of the two arguments
"""
def myfun(x, y): return x+y
# here nothing is returned if x is odd
# lamda is used to create a function without a name


def square(x):
    return x*x


marks = [1, 2, 3, 4, 5]
squaremarks = reduce(myfun, marks)
# reduce is used to reduce the list to a single value by applying the function
# to the first two elements and then to the result and the third element and
# so on
print(squaremarks)
# square the marks
# squares=filter(myfun,marks)
# print(list(squares))
sq_alt = [x * x for x in marks]
print(sq_alt)


@cache  # this is a decorator
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


# print(fact(800))
# print(fact(900))


# def crawl(*links):
#     for link in links:
#         print(link)


def process(myfun):
    def secondary(x,y):
        print("Process")
        myfun(x,y)
        return x+y
    return secondary
        


@process
# decerator is used to add functionality to a function, it is used to add
# functionality to a function without changing the function
# decerator is a function which takes a function as an argument and returns a
# function as a return value and it is used to add functionality to a function without changing the function itself and it is used to add functionality to a function without changing the function itself 
def crawl(x,y):
    print("Crawl")
    return 3                      
print(crawl(1,2))
