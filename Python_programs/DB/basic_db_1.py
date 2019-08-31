import MySQLdb

# Open the db connection
db  = MySQLdb.connect("localhost","root", "p892550878","mysql")
# Open a cursor
cursor = db.cursor()
cursor.execute("SHOW databases;")
cursor.execute("use stu")
cursor.execute("show tables")
cursor.execute("""create table student_info(
   stu_name VARCHAR(100) ,
   m1 int,
   m2 int,
   m3 int
);""")
db.close()
