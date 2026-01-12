#using normal function
# def square(x):
#   a=x*x
#   print(a)
# square(5)  

#using lambda function
# square=lambda x:x*x
# print(square(5))

#another example for calculating average
# avg=lambda x,y:(x+y)/2
# print(avg(4,6))

#another example for 3 arguments
# avg=lambda x,y,z:(x+y+z)/3
# print(avg(4,6,8))

#lambda fxn of cube of number plus 6
a=lambda x:(x*x*x)+6
print(a(2))