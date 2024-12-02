import time
print(time.strftime('%H : %M : %S'))
print(type(time.strftime('%H')))
if((int(time.strftime('%H')))>12):
    print("Good Afternoon")
else:
    print("Good Morning")
