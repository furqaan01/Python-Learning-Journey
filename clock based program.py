a=int(input("hour:"))

if(a<=12 and a>=6):
  print("GOOD MORNING")
elif(a>0 and a<24):
 if(a>12 and a<16):
  print("GOOD AFTERNOON")
 elif(a>16 and a<24):
   print("GOOD EVENING")
 elif(a>=0 and a<6):
   print("GOOD NIGHT")
else:
   print("Invalid Input")
   
  
