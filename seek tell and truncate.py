#we can also specify how much characters read functionn will read
# f=open("myfile.txt","r")
# a=f.read(6)
# print(a)

#seek function se ham kisi specified point se function read kr skte hai
# f=open("myfile.txt","r")
# f.seek(3)
# a=f.read()
# print(a)


#tell function hamme btata hai ki seek kitna kiya gaya hai
# f=open("myfile.txt","r")
# f.seek(3)
# print(f.tell())
# a=f.read()

# print(a)

#truncate function se ham kisi limit tk print kara skte hai
# f=open("myfile.txt","w")
# f.write("Hello World")
# f.truncate(5)
# f.close()

#another way
# with open("myfile.txt","w") as f:
#   f.write("hello bear")
#   f.truncate(5)
# with open("myfile.txt","r") as f:
#   a=f.read()
#   print(a)





