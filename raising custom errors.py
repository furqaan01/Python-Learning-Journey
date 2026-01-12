#error handling
# num=[1,3,6,8]
# a=int(input("enter number between 0 and 3 :"))
# print(num[a])
# if(a<0 or a>3):
#   raise IndexError("input out of range")

#another example
a=int(input("enter number between 0 and 3 :"))
if(a<0 or a>3):
  raise ValueError("input out of range")
