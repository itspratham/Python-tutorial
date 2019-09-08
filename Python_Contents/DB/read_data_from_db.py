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
        if self.m1 > 35 and self.m2 > 35 and self.m3 >35 and self.total > 150:
            return "Pass"
        else:
            return "Fail"

    def display(self):
        self.cal_total()
        self.cal_avg()

        print("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(self.name,self.m1,self.m2,self.m3,self.total,self.avg,self.result()))


# Read the data from the database
import MySQLdb

# Open the db connection
db  = MySQLdb.connect("localhost","root", "root","stu")
# Open a cursor
cursor = db.cursor()
cursor.execute("SELECT * FROM student_info")
st= cursor.fetchall()
for i in st:
    l = [int(i[1]),int(i[2]),int(i[1])]
    stu = Student(i[0],l)
    stu.display()
cursor.close()






