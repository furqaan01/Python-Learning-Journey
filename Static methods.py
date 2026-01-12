#Example:
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5/9
# a=TemperatureConverter()
# print(a.fahrenheit_to_celsius(320))
# print(a.celsius_to_fahrenheit(67))

#Another Example
# class MyClass:
#     @staticmethod
#     def my_static_method(arg1, arg2):
#         # Static method logic here
#         return arg1 + arg2
# a=MyClass()

# print(a.my_static_method(1,4))

#Another example
class data:
  @staticmethod
  def phone(m,p):
    model=m
    price=p
    print(model,price)
a=data()    
a.phone("realme",12999)
