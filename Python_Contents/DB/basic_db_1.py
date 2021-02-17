import MySQLdb

# Open the db connection
db = MySQLdb.connect("localhost", "root", "261328", "sql_exercise_01")
# Open a cursor
cursor = db.cursor()
cursor.execute("SHOW databases;")
ff = cursor.execute("show tables")
