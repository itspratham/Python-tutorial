import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

def worker():
    logging.debug("Start")
    time.sleep(2)
    logging.debug("Exit")

def service():
    logging.debug("Start")
    time.sleep(4)
    logging.debug("Exit")



s = threading.Thread(name="My Service", target=service)
w1 = threading.Thread(name="Worker 1", target=worker)
w2 = threading.Thread(name="Worker 2", target=worker)

s.start()
w1.start()
w2.start()