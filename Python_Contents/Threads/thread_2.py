# how to spawn a thread and start
import threading


def worker(num):
    print("Worker", num)
    return


t = []

for i in range(10):
    th = threading.Thread(target=worker, args=(i,))
    t.append(th)
    th.start()

print(t)
