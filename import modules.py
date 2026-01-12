#how import works
#so basically it adds all the code in import math to this code
#first example
# import math 
# a=math.factorial(4)
# print(a)

#2nd example'
# import math
# c=math.sqrt(81)
# print(c)

#another concept is related to importing certian/specific function in program, we do it like this,sirf yehi chalenge aur koi functon present in math ni chalega
# from math import pi,factorial
# a=factorial(5)
# print(a)

#using as keyword,ham keyword kuch b rkh sakhte h as per our choice
# import math as janu
# a=janu.sqrt(9)*janu.pi
# print(a)

#another example
# from math import pi,sqrt as m
# a=m(25)*pi
# print(a)

#another example
# from math import sqrt,factorial as f
# a=f(3)*sqrt(25)
# print(a)

#how to print every fxn prsent in any import module
# import math 
# print(dir(math))

# import pandas
# print(dir(pandas))

#we can also print  the type of any function
# import math
# print(type(math.pi))

#we can also make our own python module and use it in current program
from har import a,b,fun
print(a)
print(b)
fun()