#HYBRID INHERITANCE
# class furqan:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def show(self):
#     print(f"{self.name}--{self.age}--FURQAN")
# class unaib(furqan):
#   def __init__(self,name,age,skincolor):
#     furqan.__init__(self,name,age)
#     self.skincolor=skincolor
#   def show(self):
#       print(f"{self.name}--{self.age}--{self.skincolor}--UNAIB")
      
# class arsalan(furqan):
#   def __init__(self,name,age,skincolor,weight):
#     furqan.__init__(self,name,age)
#     self.skincolor=skincolor
#     self.weight=weight
#   def show(self):
#       print(f"{self.name}--{self.age}--{self.skincolor}--ARSALAN")  
      
# class asim(unaib,arsalan):
#   def __init__(self,name,age,skincolor,weight,height):
#     unaib.__init__(self,name,age,skincolor)
#     arsalan.__init__(self,name,age,skincolor,weight)
#     self.height=height
#   def show(self):
#     print(f"{self.name}--{self.age}--{self.skincolor}--{self.weight}--{self.height}--ASIM")
# a=asim("Furqan",22,"brown",59,"6 feet")    
# a.show()

#HEIRARCIAL INHERITANCE
# class parent:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age
#   def show(self):
#     print(f"{self.name}--{self.age}")
# class child1(parent):
#   def __init__(self,name,age,skincolor):
#     super().__init__(name,age)
#     self.skincolor=skincolor
#   def show(self):
#     print(f"{self.name}--{self.age}--{self.skincolor}")
# class child2(parent):
#   def __init__(self,name,age,skincolor):
#     super().__init__(name,age)
#     self.skincolor=skincolor
#   def show(self):
#     print(f"{self.name}--{self.age}--{self.skincolor}")
# class child3(parent):
#   def __init__(self,name,age,skincolor):
#     super().__init__(name,age)
#     self.skincolor=skincolor
#   def show(self):
#     print(f"{self.name}--{self.age}--{self.skincolor}")
# a=child3("furqan",23,"black")
# a.show()


#MODYIFYING THIS CODE
class parent:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def showdetails(self):
    print(f"{self.name}--{self.age}")
class child1(parent):
  def __init__(self,name,age,skincolor):
    super().__init__(name,age)
    self.skincolor=skincolor
  def showinfo(self):
    print(f"{self.name}--{self.age}--{self.skincolor}--child1")
class child2(parent):
  def __init__(self,name,age,skincolor):
    super().__init__(name,age)
    self.skincolor=skincolor
  def showdata(self):
    print(f"{self.name}--{self.age}--{self.skincolor}--child2")
class child3(parent):
  def __init__(self,name,age,skincolor):
    super().__init__(name,age)
    self.skincolor=skincolor
  def show(self):
    print(f"{self.name}--{self.age}--{self.skincolor}--child3")
a=child3("furqan",23,"black")
b=child1("furqan",23,"black")
c=child2("furqan",23,"black")
a.showdetails()
b.showinfo()
c.showdata()
a.show()


