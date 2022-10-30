import mysql.connector
c=mysql.connector.connect(host="localhost",user="root",password="admin",charset="utf8",database="richardmr")
curs=c.cursor()
def startscreen():

       print("hi what would you like to do ")
       print("we can either change a value in the database ")
       print("or we can enter a new value ")
       print("or we can VIEW the file")
       print("enter 1 to change a value")
       print("enter 2 to enter a new value")
       print("enter 3 to view the file")

       choice=int(input())
       
       
       if choice == 1:
              print("we are still in betamode")
       elif choice == 2:
             print("enter idno")
             n=int(input())
             print("enter name")
             n1=input()
             print("enter grade_percentage")
             n2=int(input())
             print("enter the house_colour")
             n3=input()
             curs.execute("insert into students values('{}','{}','{}','{}')".format(n,n1,n2,n3))
             c.commit()
             print("we have succesfullyy added a new identity")
       elif choice == 3:
              print("curs")
              curs.execute("select * from employee")
              dfb=curs.fetchall()
              print(dfb)

       else :
              print("please enter a valid number")
              startscreen()
              
       print("thanks for using our services")

startscreen()      




      
