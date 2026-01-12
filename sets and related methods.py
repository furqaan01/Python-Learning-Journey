#set methods
#union and update and intersection

# a={1,5,7,4,9,44,7}
# b={33,565,44,67,7}
# a.update(b)
# a.intersection_update(b)
# print(a)
# print(a.union(b))
# a.update(b)
# print(a,b)

#symettric differnce and difference update
# a={1,3,5,7,9}
# b={2,4,3,5}
# c=a.symmetric_difference(b)
# print(c)
# a.symmetric_difference_update(b)
# print(a)

#differnce and difference update
# a={1,3,5,7,9}
# b={2,4,3,5}
# print(a.difference(b))
# a.difference_update(b)
# print(a)

#isdisjoint#is superset #is subset
# a={1,2,4,6}
# b={2,4,6,8}
# print(a.isdisjoint(b))
# print(a.issuperset(b))
# print(a.issubset(b))

#add
# a={1,3,5,7}
# a.add(8)
# print(a)

#remove
# a={1,3,5,7}
# a.discard(5)
# print(a)

#pop-pops amy eleement
# a={1,3,5,7,9}
# item=a.pop()
# print(item)
# print(a)

#del
# a={1,3,5,7,9}
# b={2,4,6,8}
# del b
# print(b)

#clear
# a={1,3,5,7,9}
# a.clear()
# print(a)

#find
a={1,3,5,7,9}
if 0 in a:
  print('true')
else:
  print('false')