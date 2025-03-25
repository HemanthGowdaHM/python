import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "system",
    database = "cloth_store"         # try connecting to the "mydatabase" ,   fourth step
) 
# # first step : check the database is connected or not 
# print(mydb)


# # second step : create database 
# mycursor = mydb.cursor()
# mycursor.execute("create database mydatabase")

# # third step : show the database , return a list of your system's databases
# mycursor = mydb.cursor()
# mycursor.execute("show databases")

# for x in mycursor:
#     print(x)
    
    
# # fifth step :create table named "customers"
mycursor = mydb.cursor()
# mycursor.execute("create table customers(name varchar(25),age int)" )

# mycursor.execute("show tables")

# for x in mycursor:
#     print(x)


# # creating primary key for existing table
# mycursor.execute("ALTER TABLE customers ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY")


# # to fill a table in mysql, use th "INSERT INTO" statement
# # INSERT a record in the "customers" table

# sql = "INSERT INTO customers(name,age) VALUES (%s,%s)"
# val = [ ("peter",21),
#        ("sandy",25),
#        ("vicky",24),
#        ("wiliam",27)]

# mycursor.executemany(sql,val)

# mydb.commit()

# print(mycursor.rowcount,"record insereted.")



# mycursor.execute("select id,name,age from customers order by name ")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql = "DELETE FROM customers WHERE name='wiliam'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record deleted")

# sql = "DROP database mydatabase"
# mycursor.execute(sql)

mycursor.execute("use cloth_store")
# for x in mycursor:
#     print(x)