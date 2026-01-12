#LIST BASICS
list1=[0,1,3,5,8,True,"furi"]
# print(list1)
# print(type(list1))
#list indexing same as strng indexing
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# print(list1[5])
# print(list1[6])

#to check if given element exists in list or not
# if "furi" in list1:
#   print("yes")
# else:
#   print('no')

#same applies to strngs as well
# if "fu" in "furi":
#   print("yes")
# else:
#   print("no")

#printing each eleemnt of list in multiple ways
# print(list1)
# print(list1[:])
# print(list1[1:-1]) #to print specified range

#list comprehension
# list1=[i*i for i in range(10)]
# print(list1)
#badal example
# list1=[i*i for i in range(11) if i%2==0]
# print(list1)

#questons on list comprehension
#to remove odd numbers
# numbers = [3,5,45,97,32,22,10,19,39,43]
# list1=[i for i in numbers if i%2==0]
# print(list1)

#no.s divisible by 7
# list=[7*i for i in range(1000)]
# print(list)

