#recursion

def factorial(n):
  if(n==0 or n==1):
   return 1
  else:
    return n*factorial(n-1)
print(factorial(4))    
print(factorial(6))    
print(factorial(5))    

#another example
def fabonacci(n):
  if n<=1:
    return 1
  else:
    return (fabonacci(n-1)+fabonacci(n-2))
for i in range(10):
  print(fabonacci(i))