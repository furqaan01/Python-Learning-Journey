#MAP function by defining a function
# def cube(a):
#   return a*a*a
# l=[1,3,5,7]
# newl=list(map(cube,l))
# print(newl)

#MAP fxn using lambda
# l=[1,2,3,4]
# newl=list(map(lambda x:x*x*x,l))
# print(newl)


#FILTER using normal function
# def saaf(x):
#    return x>3
# l=[1,2,3,4,5,6,7]
# newl=list(filter(saaf,l))
# print(newl)

#FILTER using Lambda
# l=[1,3,5,7,8]
# newl=list(filter(lambda x:x>4,l))
# print(newl)

#REDUCE using normal function
# from functools import reduce
# def summ(x,y):
#   return x+y
# l=[1,3,5,7]
# newl=reduce(summ,l)
# print(newl)

#REDUCE using lambda
from functools import reduce
l=[1,2,3,4]
newl=reduce(lambda x,y:x+y,l)
print(newl)