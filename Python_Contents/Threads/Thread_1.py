# how to spawn a thread and start
# https://www.tutorialspoint.com/python/python_multithreading.htm
# https://www.python-course.eu/threads.php
# import threading
#
#
# def worker():
#     print("Worker")
#     return
#
#
# t = []
#
# for i in range(5):
#     th = threading.Thread(target=worker)
#     t.append(th)
#     th.start()

import concurrent.futures


def foo(bar):
    print('hello {}'.format(bar))
    return 'foo'


def foo1(bar):
    print('hello {}'.format(bar))
    return 'foo'


with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo, 'world!')
    future1 = executor.submit(foo1, 'world1!')
    return_value = future.result()
    return_value1 = future1.result()
    print(return_value)
    print(return_value1)
