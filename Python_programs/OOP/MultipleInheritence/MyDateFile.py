class MyDate(object):

    def __init__(self, d,m,y):
        self.date = d
        self.month = m
        self.year = y

    def display(self):
        print("Date is {}/{}/{}".format(self.date, self.month, self.year))

