#WAP a program to enter student details in a csv file
#containing rollnumber name class and mark and
#display students having mark greater than 75


import csv
import timerbhaimoduleimp as th
def enterring(roll,name,clas,mark): 
      with open("student.csv",'a',newline="") as f1:
            c=csv.writer(f1)
            L=[roll,name,clas,mark]
            c.writerow(L)
      th.ty("thank you the process is done")
      startscreen()
def bfenterring():
      th.ty("please enter the roll you would like to enter")
      a=input(">>>")
      th.ty("please enter name of the student")
      b=input(">>>")
      th.ty("please enter the class ")
      c=input(">>>")
      th.ty("please enter the marks scored by the student")
      d=input(">>>")
      enterring(a,b,c,d)

def reading():
      with open("student.csv",'r',newline="") as f1:
            r=csv.reader(f1)
            for i in r:
                  print(i)

      startscreen()
def filterred():
      with open("student.csv",'r',newline="") as f1:
            
      
      
             
def startscreen():
      th.ty("welcome to my program")
      th.ty("if you want to enter a value into the record type 1")
      th.ty("if u want to view the current file type 2")
      th.ty("if u want to see the number of students with marks greater than 75 type 3")
      choice=input(">>>")
      if choice > "3":
            th.ty("please enter a valid option")
            startscreen()
      elif choice == "1":
            th.ty("proceeding to enter a new record")
            bfenterring()

      elif choice == "2":
            th.ty("proceeding to view the current csv file")
            reading()

      elif choice == "3":
            th.ty("proceeding to filter to students having marks greater than 75 only")
            filterred()
startscreen()      

