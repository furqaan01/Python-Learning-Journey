#f strings

# name="talib"
# state="j&k"
# print(f"my name is {name} and I live in {state}")

# #another e.g

# price=46.0999
# text=f'cost is {price:.3f} dollaars'
# print(text)
# (.3f)used above is used to print three values after decimal


#doc string
#written right below the function definition
def isgreater(a,b):
  '''takes two numbers,returns the largest between two numbers'''
  if(a>b):
    print(a,"is greater")
  else:
    print(b,"is greater")
isgreater(4,578)
print(isgreater.__doc__)#this represents the doc string which helps to undrstand the undergoing process