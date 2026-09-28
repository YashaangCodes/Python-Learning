# Create and execute a multiple tasks with function call

import threading
import time
import os

def walk():
    time.sleep(8)
    print("Walking the dog")
    print(f"Process ID : {os.getpid()}")

def getmail():
    time.sleep(4)
    print("Fetching the mail")
    print(f"Process ID : {os.getpid()}")

def requestapplication():
    time.sleep(2)
    print("Requesting Application")
    print(f"Process ID : {os.getpid()}")

def Booking():
    time.sleep(5)
    print("Booking Tickets")
    print(f"Process ID : {os.getpid()}")

start_time = time.time()
walk()
getmail()
requestapplication()
Booking()
end_time = time.time()
print("All tasks Completed!")
print(f"Time taken : {end_time - start_time}")