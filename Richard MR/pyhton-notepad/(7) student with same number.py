#a binary file stud containing phoneno,
#name,class and rollno display the name
#of the students who have the same phone
#no
import pickle
import timerbhaimoduleimp as th
def bfenterring():
      th.ty("please enter the phone number of the new student")
      a=input(">>>")
      th.ty("please enter name of the student")
      b=input(">>>")
      th.ty("please enter the class ")
      c=input(">>>")
      th.ty("please enter the roll number of the student")
      d=input(">>>")
      enterring(a,b,c,d)
def enterring(phoneno,name,clas,rollno): 
      with open("stud.dat",'ab') as f1:
            L=[phoneno,name,clas,rollno]
            pickle.dump(L,f1)
      th.ty("thank you the process is done")
      startscreen()
def reading():
      f1= open("stud.dat",'rb')
      try:
            while True:
                  
                  

                  r=pickle.load(f1)
                  print(r)
      except EOFError as e :
            print(e)
            startscreen()
      startscreen()
def filterred():
      L=[]
      G=[]
      f1= open("stud.dat",'rb')
      try: 
            while True:
                  r=pickle.load(f1)
                  L.append(r)
      except EOFError as e :
            print(e)
            for i in L:
                  a=i[0]
                  for g in L:
                        if g[0]==a and i[1]!=g[1]:
                              G.append(i)
                              print(f" the user that have the same phone number are ")
                              print(i,g)
                              L.remove(i)

      print("process is done,moving to startscreen")
      startscreen()
            
                  
                  
def startscreen():
      th.ty("welcome to my program")
      th.ty("if you want to enter a student into the record type 1")
      th.ty("if u want to view the current file type 2")
      th.ty("if u want to see the number of students with same phoneno type 3")
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
            th.ty("proceeding to filter to students having same phone no only")
            filterred()
      else:
            print("incorrect value recieved, please try again")
            startscreen()
startscreen()      


