import mysql.connector

# Creating connection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Bhi2301"
)

# Printing the connection object
print(mydb)