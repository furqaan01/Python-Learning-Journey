#making a folder and thn making folders in folder using OS module
# import os
# os.mkdir("Data")
# for i in range(1,1001):
#   os.mkdir(f'Data\Day{i}')


#if the folder exists thn we wll use the check and thn add folders to folder
# import os
# if(not os.path.exists("Data"))
# os.mkdir("Data") 
# for i in range(1,101):
#   os.mkdir(f'Data\Day{i}')

#if we hav to add folder to folder in folder
# import os
# for i in range(1,101):
#   os.mkdir(f'Data\Day1\Tutorial{i}')

#if we have to rename the created foldrs......isme rename mai phla source aur dosra destination maana jata hai
# import os
# for i in range(1,101):
#   os.rename(f'Data\Day{i}',f'Data\Tutorial{i}')

#if hamme ab agar space add krni ho totourial mia tou ham is tarah karege
# import os
# for i in range(1,101):
#  os.rename(f'Data\Tutorial{i}',f'Data\Tutorial {i}')

# now we will print all the folders in folder
# import os
# f=os.listdir("Data")
# print(f)

#how to print all the folders and files in a folder(idhar phle ham print krte h kon konse folderrs h ek folder m,fir us folder m loop lagate hai aur print krte h uss mai prsent file or folder
# import os
# f=os.listdir("Data")
# for i in f:
#   print(i)
#   print(os.listdir(f'Data\{i}')

#how to print the current directory we are in (getcwd gives the location and chdir is used to change the location)
# import os
# a=os.getcwd()
# print(a)

# import os
# a=os.chdir("/Users")
# print(a)

#we can also delete directory
import os
directory="Data"
parent="C:\Users\furqa\OneDrive\Desktop\Learning OS module"
path=os.path.join(parent,directory)
os.rmdir(path)

