import MySQLdb

# Open the db connection
db  = MySQLdb.connect("localhost","root", "password","mysql")
# Open a cursor
cursor = db.cursor()
cursor.execute("SHOW databases;")
cursor.execute("use stu")
cursor.execute("show tables")

