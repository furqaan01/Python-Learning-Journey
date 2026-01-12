#Operator Overloading for vectors
# class vector:
#   def __init__(self,i,j,k):
#     self.i=i
#     self.j=j
#     self.k=k
#   def show(self):
#     print (f"{self.i}i + {self.j}j + {self.k}k")
#   def __add__(self,other):
#     return (f"The sum vector is equal to :{self.i+other.i}i + {self.j+other.j}j + {self.k+other.k}k")
# a=vector(5,6,7)
# b=vector(2,3,4)
# a.show()
# b.show()

# print(a+b)

#another example for complex numbers
class complex:
  def __init__(self,r,i):
    self.real=r
    self.imaginary=i
  def __str__(self):
    return (f"{self.real} + {self.imaginary}i")
  def __add__(self,other):
    return (f"{self.real+other.real} + {self.imaginary+other.imaginary}i")
a=complex(5,8)
b=complex(3,5)
print(str(a))
print(str(b))
print(a+b) 