import mysql.connector
# Open the db connection
db  = mysql.connector.connect("localhost","root", "password","python_mysql")
# Open a cursor
cursor = db.cursor()


with open("hello") as fo:
    for line in fo:
        #print(line)
        l=line.split(",")
        #print(l)
        cursor.execute("INSERT INTO hello VALUES('{}','{}');".format(l[0],int(l[1]),int(l[2])))

cursor.execute("commit;")
cursor.execute("SELECT * FROM hello;")
for i in cursor.fetchall():
    print(i)
cursor.close()
