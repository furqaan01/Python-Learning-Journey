# a=int(input("enter first number : "))
# b=int(input("enter second number : "))
# a=4
# b=3
# sign=input("enter your symbol : ")
# match sign:
#   case "+":
#     print("your sum is",int(a)+int(b))
#   case "-" :
#     print("your difference is",int(a)-int(b))
#   case "*" :  
#     print("your product is",int(a)*int(b))
#   case "/" : 
#     print("your divison is",int(a)/int(b))
#   case "**" : 
#     print("your exponent  is",int(a)**int(b))
#   case "//" :  
#     print("your floor division is",int(a)//int(b))
#   case "%" :
#     print("your modulus is",int(a)%int(b))

#to check whther number is even or odd or zero 
# a=int(input("enter your input : "))
# match a:
#   case 0:
#     print("your number is zero")
#   case a if a%2==0:
#     print("your number is even")
#   case a if a%2==1:
#     print("your number is odd")

# to check number 
a=int(input("enter your input: "))
match a:
  case 0:
    print("your number is zero")
  case a if a<10 and a>0:
    print("number lies between 0 and 10")
  case a if a>10 and a<50:
    print("number lies between 10 and 50 and square of",a,'is equal to',a*a)
  case a if a>50 and a<1000:
    print("your number lies betweeen 50 and 1000")
  case _:
    print("enter valid input!!!")
