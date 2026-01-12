#Instance variable(preferrred whn objects hav unique data)
# class student:
#   def __init__(self,name):
#     self.name=name
#     self.rise_amount=20000
#   def show(self):
#     print(f"The imcome of {self.name} is increased by {self.rise_amount}")
# a=student("Furqan")
# a.rise_amount=30000
# a.show()
# b=student("Unaib")
# b.show()

#Class variable(preferred whn all objects(instances) hav same data)
class employee:
  company="Intel"   #class variable
  def __init__(self,name):
    self.name=name    #instance variable
    self.rise="20%"   #instance variable
  def show(self):
    print(f"{self.name} has hike of {self.rise} in {self.company}")
a=employee("Furqan")
a.rise="290%"      #changed instance variable
a.company="Apple"   #changed classs variable for pearticular isntance
b=employee("Hafidd")
a.show()
b.show()





