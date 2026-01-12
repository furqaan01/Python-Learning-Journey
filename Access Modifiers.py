#Public access modifier(as it was accessible outside class easily)
# class employee:
#   def __init__(self):
#     self.name="harry"
# a=employee()
# print(a.name)    

#Private Access Modifier(directly not accesible outside class)
# class employee:
#   def __init__(self):
#     self.__name="harrybhai"
# a=employee()
# print(a.__name)    #will raise an error because we made it a private access modifier and it is not accesibble directly outside class
#to access it do as follows:
# print(a._employee__name)

#Protected access modifier
class employee:
  def __init__(self):
    self._name="furqan"
  def _show(self):
    return "code with furi"
class teacher(employee):
  pass
a=employee()
b=teacher()
print(a._name)  
print(a._show())  
print(b._name)  
print(b._show())  