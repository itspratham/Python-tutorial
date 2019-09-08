class MyTime(object):

    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def display(self):
        print("Time is {}:{}:{}".format(self.hour,self.minute,self.second))

