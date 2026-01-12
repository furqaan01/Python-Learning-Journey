a=int(input("enter your  max range : "))
for i in range(1,a,2):
  print(i)
  if(i<20):
    print("it lies between 0 and 20")
  elif(i<40 and i>20):
    print("Number lies betweeen 20 and 40")
  else:
    print("number is greater than 40")