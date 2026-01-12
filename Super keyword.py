class student:
  def __init__(self,name,id):
    self.name=name
    self.id=id
class programmer(student):
  def __init__(self,name,id,lang):
   super().__init__(name,id)
   self.lang=lang
a=programmer("furi",20,"english")
print(a.name)
print(a.id)
print(a.lang)
   