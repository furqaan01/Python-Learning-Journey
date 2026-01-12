# x=5 # global variable bcz we can use it outside the function and inside the function as well as shown below in line 3 and line 7
# def fun():
#   print(x)
  # y=2 # local variable n can be used only inside the function ,if it is used outsise the function it raises the error as shown in line 8
#   print(y)
# fun()
# print(x)
# print(y)# leadds to errror coz it is a local varibale tht can be ussed inside the function only

#now using global keyword
x=10
#global variable
def wel():
  global x 
  x=5
  #ooper wali do lines mai x=10 ka value x=5 hua by using global keyword
  y=2
  print(x)
  print(y)
wel()
print(x)  
#so basically we changed the global x value from inside the function