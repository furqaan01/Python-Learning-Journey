def mydata():
  for i in range(50000):
    yield(i)
a=mydata()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#if we want all at once so 
for k in a:
  print(k)
    










