import mysql.connector
c=mysql.connector.connect(host="localhost",user="root",password="admin",
                          charset="utf8",
                          database="richardmr")
curs=c.cursor()
n1=()
def get(n):
        print("1.show list")
        print("2.search by name")
        print("3.see employee with designation")
        print("4.add a new employee")
        global n1
        n1=int(input('enter the number(1,2,3,4)'))
get()
if n1==2:
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
               

