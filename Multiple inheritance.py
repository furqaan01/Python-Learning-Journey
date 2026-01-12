# class teacher:
#   def __init__(self,name):
#     self.name=name
#   def show(self):
#     print(f"My name is {self.name}")
# class hod:
#   def __init__(self,age):
#     self.age=age
#   def show(self):
#     print(f"My age is {self.age}")
# class student(teacher,hod):
#   def __init__(self,name,age,skincolor):
#     self.name=name
#     self.age=age
#     self.skincolor=skincolor
    
  
# a=student("Furqan",21,"black")    
# a.show()
# print(student.mro())



#ANOTHER EXAMPLE
class animal:
  def __init__(self,name,species):
    self.name=name
    self.species=species
  def soundmade(self):
    print("Animal 1 is :")
class mammal:
  def __init__(self,name,fur):
    self.name=name
    self.fur=fur
  def soundmade(self):
     print("Animal 2 is :")
class dog(animal,mammal):
  def __init__(self,name,breed,fur,species):
    animal.__init__(self,name,species)
    mammal.__init__(self,name,fur)
    self.breed=breed
  def soundmade(self):
    super().soundmade()
    print(f"{self.name} is {self.breed} of {self.fur} color and is {self.species}")
a=dog("Bruno","shepherd","black","Dog")    
a.soundmade()    