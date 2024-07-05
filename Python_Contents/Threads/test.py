import threading
import time


def worker():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(2)
    print(threading.currentThread().getName(), "Exit")


t = []

for i in range(10):
    worker()
