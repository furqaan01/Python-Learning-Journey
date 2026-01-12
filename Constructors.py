#Constructors
# class student:
#   def __init__(self,a,b):
#     self.name=a
#     self.age=b
#   def data(self):
#     print(f"{self.name} is {self.age} years old")
# x=student("furqan",22)
# x.data()
# y=student("Hafid",21)
# y.data()


#Default constructors(takes only 1 argument that is self)
# class happy:
#   def __init__(self):
#     print("Hi I m here waiting for your input")
# a=happy()    

#Parameterized constructors
class employee:
  def __init__(self,name,id,occupation):
    self.name=name
    self.id=id
    self.occupation=occupation
  def show(self):
    print(f"{self.name} with id {self.id} is a {self.occupation}")
a=employee("Furqan",210320,"HR")   
b=employee("Anan",210302,"Professor")
a.show()
b.show()


  
  