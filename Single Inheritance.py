# single level inheritance
# class animal:
#   def __init__(self,name,breed):
#     self.name=name
#     self.breed=breed
#   def show(self):
#      print(f"{self.name} is of breed {self.breed}")
# class dog(animal):
#   def __init__(self,name,breed,color):
#     super().__init__(name,breed)
#     self.color=color
#   def showdata(self):
#     print(f"and is of color {self.color}")
#  a=dog("bruno","wild dog","black")
# a.show()
# a.showdata()

#another example:
class Shape:
  def __init__(self, color):
      self.color = color

class Circle(Shape):
  def __init__(self, color, radius):
      super().__init__(color)
      self.radius = radius
  def show(self):
    print(f"{self.color} is of radius {self.radius}")

a = Circle("Red", 5)
a.show()