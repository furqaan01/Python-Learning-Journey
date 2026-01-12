#using enumerate function to use for loop to get both the index and the value in same function
a=[1,4,5,667,89,6]
for index,mark in enumerate(a,):
  print(index,mark)

#using enumerate example from a specified index
# a=[2,4,6,8,90]
# for index,value in enumerate(a,start=2):
#   print(index,value)

#ham ye normal function se bhi kar skte hai but wo lengthy hoga jaise 
# a=[2,5,4,86,0]
# index=0
# for i in a:
#   print(f'{index} index has {i}')
#   index+=1