#How to open a file n read to it
# f=open("myfile.txt",'r')
# text=f.read()
# print(text)
# f.close()

#how to write to file
# f=open("myfile.txt",'w')
# f.write("hellowww")
# f.close()

#if the file doesnt exist and we use the write operation it creates a new file and thn writes to it
# f=open("myfile2.txt","w")
# f.write("Hi dear")
# f.close()

#how to append data in file.....isme data at end add hota hai
# f=open('myfile.txt',"a")
# f.write("jaani")
# f.close()

#file handling using with keyword
#appending using with
with open("myfile.txt","a") as f:
 f.write("ABUL")
#writing using with
with open("myfile.txt","w") as f:
  f.write("Kya bolti public!!!!")
#reading using with
with open("myfile.txt","r") as f:
  a=f.read()
  print(a)