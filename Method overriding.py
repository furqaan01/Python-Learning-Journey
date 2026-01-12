#Method Overriding
# class student:
#   def __init__(self,name):
#     self.name=name
#   def show(self):
#     print(f"My name is {self.name} std")
# class teacher(student):
#   def __init__(self,name):
#     self.name=name
#   def show(self):
#     super().show()
#     print(f"My name is {self.name} tchr")
# a=teacher("furqan")
# a.show()

#Another Example
class student:
  def show(self):
    print("Mai parent class hu")
class teacher(student):
  def show(self):
    print("mai child class hu ")
    super().show()
a=teacher()
a.show()