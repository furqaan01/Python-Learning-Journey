# a=int(input("enter you number : "))
# print("your number is",a)
# if(a<=99):
#   print("'your number is 2 digit'")
# elif(a<=999):
#   print("'your number is 3 digit'")
# else:
#   print("'your number is multi-digit'")
num=int(input("enter your number:"))
print("your number is",num)
if(num<=-1):
  print("your number is negative")
elif(num>=1):
  if(num>=1 and num<30):
    print("your number lies between 0 and 30")
  elif(num>=30 and num<=100):
    print("your number lies between 29 and 100")
  else:
    print("your number is greater than 100")
else:  
  print("your number is zero")