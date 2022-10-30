import mysql.connector
c=mysql.connector.connect(host="localhost",user="root",password="admin",
                          charset="utf8",
                          database="richardmr")
curs=c.cursor()

print("enter idno")
n=int(input())
print("enter name")
n1=input()           
print("enter grade_percentage")
n2=int(input())
print("enter the house_colour")
n3=input()

#curs.execute("update students set name='{}'where name='{}'".format(n1,n2))

curs.execute("insert into students values('{}','{}','{}','{}')".format(n,n1,n2,n3))

c.commit()


###note that the database name is richard mr and the table name is students###


