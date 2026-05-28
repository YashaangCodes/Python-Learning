import time
Current_Time = int(time.strftime('%H'))
# Morning : 4 AM to 11:59 AM
# Afternoon : 12 PM to 16:59 PM
# Evening : 17 PM to 21:59 PM
# Night : 22 PM to 3:59 AM

if 4 <= Current_Time < 12:
    print(" Good Morning ! ".center(50))
elif 12 <= Current_Time < 17:
    print(" Good Afternoon ! ".center(50))
elif 17 <= Current_Time < 22:
    print(" Good Evening ! ".center(50))
else:
    print(" Good Night ! ".center(50))