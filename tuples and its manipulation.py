#tuple(almost same as list but ye immutable hai)

# t=(1,3,5,True,"haaha")
#indexing
# print(t[0])
# print(t[1])
# print(t[0])
# print(t[-2])
#finding if element exits or not
# if True in t:
#   print("yes")
# else:
#   print("no")
# if "w" in "haaha":
#   print("yes")
# else:
#   print("no")
# print(t[1:4])
# print(t[0:5:2])
# print(t[:4])
# print(t[1:])

#OPERATIONS ON TUPLES/ MANIPULATING TUPLES

#convrting tuple in listn thn manipulating it
# tupl1=(1,3,5,7,8)
# temp=list(tupl1)
# temp.pop(2)
# temp.append(11)
# temp.insert(2,4)
# temp=tuple(temp)
# print(temp)

#another example 
# tup=("abu","ami","bhai","behn","cxn")
# new=list(tup)
# new.append("wife")
# new.pop(2)
# new.sort(reverse=True)
# tup=tuple(new)
# print(tup)

#concatinating tuples
# tup1=(1,3,5,7,8)
# tup2=("abu","ami","bhai","behn","cxn")
# tup3=tup1+tup2
# print(tup3)

#counting occurance in tuple
# tup=(1,3,5,7,9,7,2,7)
# print(tup.count(7))
# print(tup.index(9))

#for checking for second occurance and so on occurances we wll do like below
# print(tup.index(7,4,7))

#calculate lenth o tuple
tup=(1,3,5,7,9,7,2,7)
print(len(tup))