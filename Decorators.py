# #without argument example
# def message(fx):
#   def mfx():
#     print("hi ")
#     fx()
#     print("bye")
#   return mfx
# @message
# def hello():
#   print("i m here")
# hello()  

# #with argument example
# def wish(gx):
#   def mgx(*args,**kwargs):
#     print("I am ready")
#     gx(*args,**kwargs)
#   return mgx
# @wish
# def add(a,b):
#   print(a+b)
# add(2,4)  

#example for decorators for calculator
def greet(fx):
  def mfx(*args,**kwargs):
    print("Your result is")
    fx(*args,**kwargs)
    print("Thanks for accessing")
    print("Take care buddy")
  return mfx  
@greet
def cal(a,b):
 if z==1:
   print(a+b)
 elif z==2:
   print(a-b)
 elif z==3:
   print(a*b)
 elif z==4:
   print(a/b)
x=int(input("enter your 1st number : "))   
y=int(input("enter your 2nd number : "))   
print("Select Operation")
print("1:Addition")
print("2:subtraction")
print("3:multiplication")
print("4:division")
z=int(input("Enter your choice : ")) 
cal(x,y)   