class student:
  def __init__(self,name,value):
    self.name=name
    self.value=value
  @property
  def newvalue(self):
    return 10*self.value
  @newvalue.setter
  def newvalue(self,newvalue):
    self.value=newvalue/10
  def show(self):
    print(f"my name is {self.name} and my value is {self.value}")
a=student("furqan",100)
b=student("hafid",11)
a.newvalue=67
print(a.newvalue)
a.show()
b.show()