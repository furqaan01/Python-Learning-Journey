print even no. or odd no.
b=int(input("enter a no.: "))
print("your choice is : ",b)
if(b%2==0):
  print("your number is even ")
else:
  print("your number is odd")

print largest of 3 numbers
a=int(input("enter your first number: ",))
b=int(input("enter your second number: ",))   
c=int(input("enter your third number: ",))
if(a>b and a>c):
  print("the largest number is ",a)
elif(b>a and b>c):
  print("the largest number is ",b)
else:
  print("the largest number is ",c)

to check whether the person is eligible to vote or not
age=int(input("enter the age of person: "))
if(age<18):
  print("'person is not eligible to vote' ")
else:
  print("'person is eligible to vote' ")

grades based on percentage
percentage=int(input("enter students percentage : "))
if(percentage>95 and percentage<100):
  print("Student has scored A grade")
elif(percentage<95):
  if(percentage<95 and percentage>75):
    print("Student has scored B grade")
  elif(percentage<75 and percentage>35):
    print("Student has scored C grade")
  else:
    print("Student is failing")
else:
  print("Invalid percentage")

