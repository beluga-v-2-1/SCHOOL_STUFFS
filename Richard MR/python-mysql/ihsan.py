import mysql.connector
c=mysql.connector.connect(host="localhost",user="root",password="admin",
                          charset="utf8",
                          database="richardmr")
curs=c.cursor()
def search(n):
        curs.execute("select * from employee where name='{}'".format(n))
        r=curs.fetchone()
        if r is None:
               print("not present")
        else:
               print(r)
n=input("enter the name to search")
search(n)
def search(b):
       curs.execute("select name from employee where designation='{}'".format(b))
       i=curs.fetchall()
       if i is None:
              print("null")
       else:
              print(i)
b=input("enter the designation")
search(b)
               

