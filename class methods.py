#class methods
class employee:
  occupation="engineer"
  def __init__(self,name):
    self.name=name
  def show(self):
    print(f'{self.name} is a {self.occupation}')
#now changing class variable
  @classmethod
  def changeocc(cls,newocc):
    cls.occupation=newocc
a=employee("furi")
b=employee("haffu")
a.changeocc("teacher")
print(employee.occupation)
a.show()
b.show()


