# DEFAULT ARGUMENTS
# def address(lane="2",tehsil="hazratbal",district="srinagar"):
#   print("location is",lane,tehsil,district)
# address()
# if address fucntion is run alone thn the intial arguments are taken in consdiration otherwise neeche wale taken
# address(3,"hoenpora",district="anantnag")  


# KEYWORD ARGUMENTS
# isme arguments k sath unka vallue likhna zaroori hai neeche waale function mai , order matter ni krta
# def average(a=4,b=6):
#   print("average is equal to",(a+b)/2)
# average(b=12,a=8)  

# REQUIRED ARGUMENTS(JO LIKHNE ZAROORI HAI)
# def average(b,a=4,c=10,):
#   print("average is",(a+b+c)/2)
# average(b=45,)  


# VARIABLE LENGTH ARGUMENTS
# def add(*num):
#  ye banata hai ek tuple jisme ham jitne elements chahe add kr skte hai, fir iss tuple ko access krege using for loop 
#   c=0
#   for i in num:
#     c=c+i
#   print("sum is",c)
# add(2,3,4,5)  

# AVERAGE OF NUMBERS USING VARIABLE LENGTH ARGUMENT
# def average(*numbers):
#   avg=0
#   for i in numbers:
#     avg=avg+i/len(numbers)
   
#   print("average is",avg)    
# average(1,3,4,5+)

# questions on variable length arguments
# def names(*strings):
#   s=""
#   for i in strings:
#     s=s+i
#   print("string is",s)
# names(" {tutu}"," {kuku}"," {momo}"," {jojo}")    
# names("lili ","manu ","bebo ")

# another question
# def product(*numbers):
#   l=1
#   for i in numbers:
#     l=l*i
#   print("product is",l)  
# product(5,10)
# product(2,3,4,5,6)


       