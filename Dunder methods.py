#__LEN__ METHOD
# class student:
#   def __init__(self,name):
#     self.name=name
    
#   def __len__(self):
#      return (len(self.name))
# a=student("Xulfiqar")
# print(len(a))


#__STR__ & __REPR__ METHODS
# class student:
#   def __init__(self,name):
#     self.name=name
#   def __str__(self):
#      return (f"My name is {self.name} str")
#   def __repr__(self):
#      return (f"My name is {self.name} repr")
# a=student("FURI")   
# print(a)
# print(str(a))
# print(repr(a))

#CALL METHODS
class student:
  def __init__(self,name):
    self.name=name
  def __call__(self):
    print ("hi")

a=student("FURI")
a()
