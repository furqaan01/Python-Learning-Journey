# # using time.time() function
# import time
# current_time=time.time()
# print(current_time)

#Calculating execution time using time.time()
# import time
# start_time=time.time()
# for i in range(500000):
#   print(i)
# print("BYE")
# end_time=time.time()
# print(end_time-start_time)

#Pausing execution
# import time
# print("start")
# time.sleep(20)
# print("Ok bye")

#Localtime generation
# import time
# local_time=time.localtime()
# print(local_time)

#Localtime in more suitable form
# import time
# local_time=time.localtime()
# readable_time=time.asctime(local_time)
# print(readable_time)

#time.strftime
# import time
# current_time=time.localtime()
# formatted_time=time.strftime("%H:%M:%S",current_time)
# print(formatted_time)

#Working on UTC tine
# import time
# a=time.gmtime()
# print(time.asctime(a))
# print(a)

#Converting time into seconds since epoch(1970 se)
import time
a=time.localtime()
time_in_sec=time.mktime(a)
print(time_in_sec)