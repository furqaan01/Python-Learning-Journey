#palindrome program for string
# def pal(s):
#   return s==s[::-1]
# p=input("enter string value")
# if pal(p):
#   print("yes its a palindrome")
# else:
#   print("not a palindrome")

#removing duplicate numbers using function
a=[1,3,55,67,1,3]
def rd(b):
  return list(set(b))

print(rd(a))

#extract elemets from dict and store in variable and store it in fle
# a={1:"Furqan",2:"Talib",3:"Asim"}
# b=(a.values())
# c=str(b)
# # print(c)
# f=open("myfile.txt","w")
# f.write(c)
# f.close