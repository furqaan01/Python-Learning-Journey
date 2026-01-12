a="harry-12000"
n=a.split("-")
class employee:
  company="google"
  def __init__(self):
    self.name=n[0]
    self.salary=n[1]
  def show(self):
    print(f'{self.name} works in {self.company} with salary{self.salary}')
a=employee()    
a.show()