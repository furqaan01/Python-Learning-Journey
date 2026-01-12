#program explained on copy
#using readline to read multiple lines
# f=open("myfile.txt","r")
# while True:
#   line=f.readline()
#   if not line:
#     break
#   print(line)

#reading using readline(while )#idhar ham intial value aur increment dete h jo while k liye zaroori hota hai
# f=open("myfile.txt","r")
# i=0
# while True:
#   i=i+1
#   a=f.readline()
#   b=a.split(",")[0]
#   c=a.split(",")[1]
#   d=a.split(",")[2]
#   print(f'the marks of student{i} in SST is {b}')
#   print(f'the marks of student{i} in Urdu is {c}')
#   print(f'the marks of student{i} in MAth is {d}')
#   if not a:
#     break

#reading using readline(for)
# f=open("myfile.txt","r")
# for i in range(1,4):
#   a=f.readline()
#   if not a:
#     break
#   b=int(a.split(",")[0])
#   c=int(a.split(",")[1])
#   d=int(a.split(",")[2])
#   print(a)
#   print(f'the marks of student{i} in math is {b*2}')
#   print(f'the marks of student{i} in urdu is {c*2}')
#   print(f'the marks of student{i} in GK is {d*2}')
  #so basically is reading wale program mai maine file phle hi open karri aur for loop using range of lines  aur har ek line ke ek ek index ko alag value rkha fir print karra aur hamne jo type casting ki wo isiliye ki kuinki ye basically ek string ki tarah act krta h so we need to convert it into integer value

#Writelines 
# f=open("myfile.txt","w")
# lines=["\'har sans se pooch ke batade\'\n","inke faslo mai tu hai ke nahi\n","mai aas paas tere q mere pass tu hai ke nhi\n"]
# f.writelines(lines)
# f.close()

#writelines using for loop
# f=open("myfile2.txt","w")
# lines=["they","we",'us',"them"]
# for i in lines:
#   f.write(i + '\n')
# f.close()

