from functools import reduce


myfun = lambda x,y: x+y
# here nothing is returned if x is odd
# lamda is used to create a function without a name

def square(x):
    return x*x

marks=[1,2,3,4,5]
squaremarks=reduce(myfun, marks)
#reduce is used to reduce the list to a single value by applying the function to the first two elements and then to the result and the third element and so on
print(squaremarks)
# square the marks
# squares=filter(myfun,marks)
# print(list(squares))



