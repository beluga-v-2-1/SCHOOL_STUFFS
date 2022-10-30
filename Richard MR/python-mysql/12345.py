import mysql.connector
c=mysql.connector.connect(host="localhost",user="root",password="admin",
                          charset="utf8",
                          database="richardmr")
curs=c.cursor()

def input():
        opt='y'
        while opt=='y':
                e=int(input("enter adno"))
                n=input("name")
                salary=int(input("salary"))
                designation=input("designation")
R=curs.execute("insert into emoplyee value({},'{}',{},'{}')".format(adno,name,salary,designation))
c.commit()
opt=input("do you want to continue?")

def search():
        name=input("search name")
        b=curs.execute("select star from employee where name=('{}')".format(name))
        j=curs.fetchone()
        print(j)
        

def display():
        display=input("enter designation")
        c=curs.execute("select star from employee where designation='{}'".format(designation))
        k=curs.fetchall()
        print(k)
        
p=1
while p<4:
        print("enter your choice")
        print("\n1.insert\n2.search\n3.display")
        p=int(input())
        if p==1:
                input1()
        elif p==2:
                search1()
        elif p==3:
                display()
               

     
               
               
               

