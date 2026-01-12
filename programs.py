# factorial
# def fact(a):
#   if(a==0 or a==1):
#     return 1
#   else:
#     return a*fact(a-1)
# print(fact(4))    

#prime nmber
num=int(input("enter your number: "))
if num==1:
  print("neither prime nor composite")
for i in range(2,num):
  if num%i==0:
    print("not prime")
    break
else:
  print("prime")

#fibonacci series
# num=int(input("enter number : "))
# x=0
# y=1
# z=0
# while(z<=num):
#   print(z)
#   x=y
#   y=z
#   z=x+y