#Basic example of class n objects
# class student:
#   name="furqan"
#   rollno=21
#   standard=10
# a=student() 
# print(a.name,"is of",a.standard,"standard")

#How to modify the objects
# class student:
#   name="furqan"
#   rollno=21
#   standard=10
# # a=student()
# # print(a.name,"is of",a.standard,"standard")
# b=student()
# b.name="harry"
# b.standard=9
# print(b.name,"is of",b.standard,"standard")

#Another example
class student:
  name="furqan"
  rollno=2
  standard=10
  def data(self):
    print(f'{self.name} has {self.rollno} roll no and is of standard {self.standard}' )
a=student()
b=student()
c=student()
b.name="Isa"
c.name="Hafid"
b.rollno=3
c.rollno=4
a.data()
b.data()
c.data()
  
  