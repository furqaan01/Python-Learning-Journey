#Exception handling
# a=input('enter your input : ')
# print(f"the multiplication table of {a} is :")
# try:
#  for i in range(1,11):
#   print(f'{int(a)}x{i}={int(a)*i}') 
   
# except:
#   print("INVALID")

# print("hi")


#exception handling with multiple exceptions
try:
 num=int(input("enter valid index"))
 a=[3,4,6]
 print(a[num])
  
except ValueError:
  print("not vaalid input")
except IndexError:
  print("not valid index")
print("kya")  
