#dictionaries

# a={"name":'furqan',"roll no":2,"lane no.":229032}
# print(a)
# print(type(a))
# print(len(a))
# print(a['name'])

#accessing single key elements
# a={547:"furqan",548:"dar",549:"khan",550:"shah"}
# print(a[550])

#accesing multiple elements
# a={547:"furqan",548:"dar",549:"khan",550:"shah"}
# print(a.keys())              #prints all keys
# print(a.values())            #prints all values
#we can print using for loop as well
# for keys in a.keys():
#   print(a[keys])

#now using fstrings here
# a={"caste1":"mir","caste2":"dar","caste3":"khan","caste4":"shah"}
# for keys in a.keys():
#   print(f"the value of {keys} is {a[keys]}")

#prints all the items of dictionary
# print(a.items())







#practice
a={5:"dar",6:"khan",7:"mir"}
print(a.items())
print(a.keys())
print(a.values())
for keys in a.keys():
  print(keys)       #keys
  print(a[keys])   #values
  print(f"the key value of {keys} is {a[keys]}")