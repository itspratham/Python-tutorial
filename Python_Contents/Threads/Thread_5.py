import logging
import threading
import time

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s', )


class MyThread(threading.Thread):

    def run(self):
        logging.info("Running")
        return


for i in range(5):
    t = MyThread()
    t.start()
