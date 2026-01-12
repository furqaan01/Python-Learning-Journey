#re.findall()function

#literal character
# import re
# pattern=r"dog"
# text="dog is a pet animal"
# matches=re.findall(pattern,text)
# # print(matches)
# if matches:
#   print("Found: ",matches)
# else:
#   print("Not found")  

#Special characters
#1:dot
# import re
# text="cat sat on the mat"
# pattern=r".at"
# matches=re.findall(pattern,text)
# print(matches)

#2:^(caret)
# import re
# pattern=r"^cat"
# text="cat sat on the mat"
# matches=re.findall(pattern,text)
# print(matches)

#3:$(Dollar)
# import re
# pattern=r"mat$"
# text="cat sat on the mat"
# matches=re.findall(pattern,text)
# print(matches)

#4:*(Asterisk)
# import re
# pattern=r"ca*t"
# text="ct cat caat caaat caaaat rat" 
# matches=re.findall(pattern,text)
# print(matches)

#5:+(Plus)
# import re
# pattern=r"ca+t"
# text="ct cat caat caaat caaaat rat" 
# matches=re.findall(pattern,text)
# print(matches)

#6:?(Question mark)
# import re
# pattern=r"ca?t"
# text="ct cat caat caaat caaaat"
# matches=re.findall(pattern,text)
# print(matches)

#7:[](square brackets)
# import re
# text="cat bat rbat hat"
# pattern=r"[cb]at"
# matches=re.findall(pattern,text)
# print(matches)

#8:|(pipe):
# import re 
# text="cat is different from dog"
# pattern=r"cat|dog"
# matches=re.findall(pattern,text)
# print(matches)


#Escaping special characters(+,-,*,.)
# import re
# text='dog is animal.It is ruthless'
# pattern=r"\."
# matches=re.findall(pattern,text)
# print(matches)


#Common character class
#1:\d
# import re
# text="dog will be extinct in 2045."
# pattern=r"\d"
# matches=re.findall(pattern,text)
# print(matches)

#2:\D
# import re
# text="dog will be extinct in 2045."
# pattern=r"\D"
# matches=re.findall(pattern,text)
# print(matches)

#3:\w
# import re
# text="dog will be extinct in 2045_morning."
# pattern=r"\w"
# matches=re.findall(pattern,text)
# print(matches)

#4:\W
# import re
# text="dog will be extinct in 2045_morning."
# pattern=r"\W"
# matches=re.findall(pattern,text)
# print(matches)

#5:\s
# import re
# text="dog will be extinct in 2045_morning."
# pattern=r"\s"
# matches=re.findall(pattern,text)
# print(matches)

#6:\S
# import re
# text="dog will be extinct in 2045_morning."
# pattern=r"\S"
# matches=re.findall(pattern,text)
# print(matches)/


#REPEATATION QUALIFIERS
#1:{n}
# import re
# pattern=r"a{3}"
# text="aa aaa aaaa aaaaa"
# matches=re.findall(pattern,text)
# print(matches)

#2:{n,m}
# import re
# pattern=r"a{2,4}"
# text="aa aaa aaaa aaaaa"
# matches=re.findall(pattern,text)
# print(matches)





#re.search()
# import re
# text="dog is animal.dog is dirty"
# pattern=r"dog"
# matches=re.search(pattern,text)
# # print(matches.group())
# if matches:
#   print("yes found")
# else:
#   print("Not found")  




  #re.sub()
import re 
pattern=r"dog"
replace="puppy"
text="dog is big.dog is dirty"
change=re.sub(pattern,replace,text)
print(change)