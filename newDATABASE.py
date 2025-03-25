import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "system",
    database = "student"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE STUDENT(STD_ID INT AUTO_INCREMENT, NAME VARCHAR(20),STD_DOB DATE, GENDER VARCHAR(6),CLASS VARCHAR(5),PRIMARY KEY(STD_ID))")

# mycursor.execute("ALTER TABLE STUDENT AUTO_INCREMENT =100")

# sql ="INSERT INTO STUDENT(NAME,STD_DOB,GENDER,CLASS) VALUES (%s,%s,%s,%s)"
# val = ("HEMANTH","2003-02-16","MALE","8SEM")

# mycursor.execute(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"row inserted.")

myresult = mycursor.fetchone()
for x in myresult:
    print(x)