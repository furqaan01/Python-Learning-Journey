#Inheritance
class student:
  def __init__(self,name,id):
     self.name=name
     self.id=id 
  def show(self):
    print(f"{self.name} has ID {self.id}")
class office(student):
    def showdata(self):
        print("OK BYE")  

# a=student("Furqan",210320) 
b=office("Ibaad",210315)

b.show()
b.showdata()



