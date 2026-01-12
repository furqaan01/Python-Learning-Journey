class grandparents:
  def __init__(self,name1,name2):
    self.name1=name1
    self.name2=name2
  def show(self):
    print("GENERATIONS====>")
    print(" ")
    print("<<GRANDPARENTS>>")
    print(f"1:Dadu-{self.name1}")
    print(f"2:Dadi-{self.name2}")
    print(" ")
class parents(grandparents):
  def __init__(self,name1,name2,name3,name4):
    grandparents.__init__(self,name1,name2)
    self.name3=name3
    self.name4=name4
  def show(self):
    grandparents.show(self)
    print("<<PARENTS>>")
    print(f"3:Papa-{self.name3}")
    print(f"4:Mama-{self.name4}")
    print(" ")
class generation(parents):
  def __init__(self,name1,name2,name3,name4,name5,name6):
    parents.__init__(self,name1,name2,name3,name4)
    self.name5=name5
    self.name6=name6
  def show(self):
    parents.show(self)
    print("<<SIBLINGS>>")
    print(f"5:Brother-{self.name5}") 
    print(f"6:Sister-{self.name6}")
    print(" ")
    print("END")
a=generation("Mohd. Amin Dar","Hafeeza","Shabir ahmad","Mymoona","Furqan","Muskan") 
a.show()
print(generation.mro())