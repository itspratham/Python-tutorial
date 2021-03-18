class Student(object):

    def __init__(self, name, mrks):
        self.name = name
        self.m1 = mrks[0]
        self.m2 = mrks[1]
        self.m3 = mrks[2]
        self.total = 0
        self.avg = 0

    def cal_total(self):
        self.total = self.m1 + self.m2 + self.m3

    def cal_avg(self):
        self.avg = self.total / 3

    def result(self):
        """
        individual mark is  > 35
        total is  more than 150
        :return:
        """
        if self.m1 > 35 and self.m2 > 35 and self.m3 > 35 and self.total > 150:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        self.cal_total()
        self.cal_avg()

        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.name, self.m1, self.m2, self.m3, self.total, self.avg,
                                                    self.result()))


with open("student.csv") as fo:
    for line in fo.readlines():
        lst = line.split(",")
        stu = Student(lst[0], [int(x) for x in lst[1:4]])
        stu.display()
