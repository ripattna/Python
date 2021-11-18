import mysql.connector as c

con = c.connect(host="localhost", user="root", password="root", database="demo")

if con.is_connected():
    print("Successfully Connected..")
else:
    print("Some  Connection Issue...")

# prepare a cursor object using cursor() method
cursor = con.cursor()

# execute SQL query using execute() method.
cursor.execute("show databases")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()
print(data)

for x in data:
    print("The database available are:", x)

# disconnect from server
con.close()
