#employee= empno, name, salary, department
#make a program to make a table and
#show the number of employees per department
import mysql.connector
c=mysql.connector.connect(host="localhost",
                          user="root",
                          password="admin",
                          charset="utf8")
curs=c.cursor()


def startscreen():
       print("+--------------------------------------------+")
       print("|Hello welcome to my program                 |")
       print("+--------------------------------------------+")
       print()
       print("+--------------------------------------------+")
       print("|To view the current table           type 1  |")
       print("|To enter a new employee             type 2  |")
       print("|To view no of employee              type 3  |")
       print("|To end this endless loop            type 4  |")
       print("+--------------------------------------------+")
       choice=input(">>>")
       if choice=="1":
         
         view()
       elif choice=="2":
         inputer()
       elif choice=="3":
         finder()
       elif choice=="4":
         print("exiting program")
         exit()

def finder():
  curs.execute("use employee_database")
  curs.execute("select count(*) , department from employee group by department")
  x=curs.fetchall()
  for i in x:
    print(i)  
  startscreen()
  
def inputer():
  curs.execute("use employee_database")
  print("enter empno")
  n=int(input(">>>"))
  print("enter name")
  n1=input(">>>")           
  print("enter salary")
  n2=int(input(">>>"))
  print("+-----------------------+")
  print("|enter the department   |")
  print("+-----------------------+")
  print("+-----------------------+")
  print("|R&D            type 1  |")
  print("|SECURITY       type 2  |")
  print("|MEDICAL        type 3  |")
  print("|ACCOUNTING     type 4  |")
  print("|IT             type 5  |")
  print("+-----------------------+")
  nn3=input(">>>")
  if nn3=="1":
    n3="R&D"
  elif nn3=="2":
    n3="SECURITY"
  elif nn3=="3":
    n3="MEDICAL"
  elif nn3=="4":
    n3="ACCOUNTING"
  elif nn3=="5":
    n3="IT"
  #curs.execute("update students set name='{}'where name='{}'".format(n1,n2))
  curs.execute("insert into employee values('{}','{}','{}','{}')".format(n,n1,n2,n3))
  c.commit()
  print("would you like to add more ?")
  print("type Y or N")
  mybean=input(">>>")
  if mybean.lower()=="y":
    inputer()
  elif mybean.lower()=="n":
    startscreen()
  else:
    print("incorrect input found, moving back to main menu")
  ###note that
def view():
  curs.execute("use employee_database")
  curs.execute("select * from employee")
  x=curs.fetchall()
  for i in x:
    print(i)
  startscreen()
def startscreener():
  
  print("+--------------------------------------------+")
  print("|Hello welcome to my program                 |")
  print("+--------------------------------------------+")
  print()
  print("+--------------------------------------------+")
  print("|To go to main program               type 1  |")
  print("|To install this program             type 2  |")
  print("|To end this endless loop            type 3  |")
  print("+--------------------------------------------+")
  choice=input(">>>")
  if choice=="1":
        startscreen()
  elif choice=="2":
        startup()
  elif choice=="3":
        print("exiting program")
        exit()
  else:
        print("please enter a valid option(either '1'or'2'or'3')")
        startscreener()
def startup():
  try:
    curs.execute("create database employee_database")
    startup1()
  except mysql.connector.errors.DatabaseError as e:
    startup1()
def startup1():
  try:
    curs.execute("use employee_database")
    curs.execute("create table employee(empno int(10),name varchar(15),salary int(10),department varchar(30))")
    c.commit()
    startscreen()
    
  except mysql.connector.errors.ProgrammingError as e:
    print("the program already exists in your computer")
    startscreen()
startscreener()






































































































