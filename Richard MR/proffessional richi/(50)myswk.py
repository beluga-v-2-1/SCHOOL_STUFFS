#create a table roll no name
#class and mark. display the
#display the students name
#and class of all the students
#whose mark is in the range
#50 to 75
import mysql.connector
c=mysql.connector.connect(host="localhost",
                          user="root",
                          password="admin",
                          charset="utf8")
curs=c.cursor()
def inputer():
  curs.execute("use school_system")
  print("enter rollno")
  n=int(input(">>>"))
  print("enter name")
  n1=input(">>>")           
  print("enter class")
  n2=int(input(">>>"))
  print("enter the mark")
  n3=input(">>>")
  #curs.execute("update students set name='{}'where name='{}'".format(n1,n2))
  curs.execute("insert into students values('{}','{}','{}','{}')".format(n,n1,n2,n3))
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
  ###note that the database name is richard mr and the table name is students###
def finder():
  curs.execute("use school_system")
  curs.execute("select name, class from students where mark between 50 and 75")
  x=curs.fetchall()
  for i in x:
    print(i)  
  startscreen()
def view():
  curs.execute("use school_system")
  curs.execute("select * from students")
  x=curs.fetchall()
  for i in x:
    print(i)
  startscreen()
def updater():
    curs.execute("use school_system")
    curs.execute("select * from students")
    x=curs.fetchall()
    for i in x:
      print(i)
    print("who would you like to update")
    print("please enter a roll no")
    x=input(">>>")
    curs.execute("select * from students where rollno='{}'".format(x))
    fine=curs.fetchall()
    print(f"would you like to update the marks of {fine} ?")
    print("type y to continue")
    print("type n to enter a diffrent roll number")
    finer=input(">>>")
    if finer.lower()=="y":
      print("enter a number to replace the mark with...")
      choicer=input(">>>")
      curs.execute("update students set mark='{}' where rollno='{}'".format(choicer,x))
      c.commit()
      print("process done")
      print("would you like to update more students ?")
      print("type y to update more")
      print("type n to go back to main menu")
      elite=input(">>>")
      if elite.lower()=="y":
        updater()
      elif elite.lower()=="n":
        startscreen()
    elif finer.lower()=="n":
      print("type 1 to go enter a new value")
      print("type 2 to go to the main menu")
      sinewave=input(">>>")
      if sinewave=="1":
        updater()
      elif sinewave=="2":
        startscreen()
      else:
        print("invalid option detected")
        print("moving to main menu")
        startscreen()
    else:
      print("invalid choice detected")
      print("moving to main menu")
      startscreen()
def remover():
  try:
    curs.execute("use school_system")
    curs.execute("select * from students")
    x=curs.fetchall()
    for i in x:
      print(i)
    try:
      print("enter the roll number of the person you")
      print("want to remove")
      x=input(">>>")
    except ValueError as e:
      print("please enter a valid charector")
      remover()
    curs.execute("select rollno, name from students where rollno={}".format(x))
    xender=curs.fetchall()
    print(f"do you want to remove {xender} from the table ?")
    print("type Y or N")
    choice=input(">>>")
    if choice.lower()=="y":
      curs.execute("delete from students where rollno='{}'".format(x))
      c.commit()
      print("process done moving back to main menu")
      startscreen()
    elif choice.lower()=="n":
      print("do you want to enter a new admission number or go back to main menu")
      print("type 1 to enter a new admission number")
      print("type 2 to go back to main menu")
      file=input(">>>")
      if file.lower()=="1":
        remover()
      elif file.lower()=="2":
        startscreen()
    else:
      print("moving back to main menu")
      startscreen()
  except mysql.connector.errors.ProgrammingError as e:
    print("please enter a valid option")
    remover()
def finewine():
  curs.execute("use school_system")
  curs.execute("select * from students order by class,name asc")
  x=curs.fetchall()
  for i in x:
    print(i)
  startscreen()
def startup():
  try:
    curs.execute("create database school_system")
  except mysql.connector.errors.DatabaseError as e:
    startup1()
def startup1():
  try:
    curs.execute("use school_system")
    curs.execute("create table students(rollno int(10),name varchar(15),class int(2),mark int(3))")
    c.commit()
    startscreen()
  except mysql.connector.errors.ProgrammingError as e:
    print("the program already exists in your computer")
    startscreen()
def startscreener():
       print("+--------------------------------------------+")
       print("|Hello welcome to my program                 |")
       print("+--------------------------------------------+")
       print()
       print("+--------------------------------------------+")
       print("|To view the current table           type 1  |")
       print("|To enter a new student              type 2  |")
       print("|To view marks between 50 and 75     type 3  |")
       print("|To install this program             type 4  |")
       print("|To end this endless loop            type 5  |")
       print("+--------------------------------------------+")
       choice=input(">>>")
       if choice=="1":
              view()
       elif choice=="2":
              inputer()
       elif choice=="3":
              finder()
       elif choice=="4":
               startup()
       elif choice=="5":
               print("exiting program")
               exit()
       else:
              print("please enter a valid option(either '1'or'2'or'3'or'4')")
              startscreen()
def startscreen():
       print("+--------------------------------------------+")
       print("|Hello welcome to my program                 |")
       print("+--------------------------------------------+")
       print()
       print("+--------------------------------------------+")
       print("|To view the current table           type 1  |")
       print("|To enter a new student              type 2  |")
       print("|To view marks between 50 and 75     type 3  |")
       print("|To update the marks of a student    type 4  |")
       print("|To delete a student from the table  type 5  |")
       print("|To view the table in asc order      type 6  |")
       print("|To end this endless loop            type 7  |")
       print("+--------------------------------------------+")
       choice=input(">>>")
       if choice=="1":
         view()
       elif choice=="2":
         inputer()
       elif choice=="3":
         finder()
       elif choice=="4": 
         updater()
       elif choice=="5":
         remover()
       elif choice=="6":
         finewine()
       elif choice=="7":
         print("exiting program")
         exit()  
startscreener()               
