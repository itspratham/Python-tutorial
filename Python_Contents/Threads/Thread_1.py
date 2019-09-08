# how to spawn a thread and start
# https://www.tutorialspoint.com/python/python_multithreading.htm
#https://www.python-course.eu/threads.php
import threading

def worker():
    print("Worker")
    return

t = []

for i in range(5):
    th = threading.Thread(target=worker)
    t.append(th)
    th.start()