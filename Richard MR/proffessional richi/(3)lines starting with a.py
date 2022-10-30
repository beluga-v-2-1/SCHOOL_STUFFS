#write a program to insert a
#string in a text file and display
#the lines which are starting with ‘A’
#also display the number of
#ines starting with ‘A’.
f1=open("student.txt",'r')
f2=open("student.txt",'a')
def view():
       with open("student.txt",'r') as f3:
              new=f3.read()
              print(f"{new}")
       startscreen()       
def insert():
       with open("student.txt",'a') as f2:
              print("lets insert stuff")
              print("what would you like to insert into the file ?")
              inserth=input(">>>")
              inserth+="\n"
              try:
                     print("are you sure to insert this? (y/n)")
                     nos=input(">>>")
                     if nos.lower()=="y":
                           f2.write(inserth)
                           print("your word has been inserted into text")
                     elif nos.lower()=='n':
                           print('lets start again')
                           insert()
                     else:
                           print("please enter a valid option (either y or n)")
                           insert()
              except EOFError as e:
                     print(e)
       startscreen()
def check():
       print("currently under development")
       startscreen()
def end():
       print("end of loop")
       exit()  
def startscreen():
       print("+--------------------------------------------+")
       print("|Hello welcome to my program                 |")
       print("+--------------------------------------------+")
       print()
       print("+--------------------------------------------+")
       print("|To insert a string into a text file type 1  |")
       print("|To view the number of lines with'a' type 2  |")
       print("|To view the file you are working on type 3  |")
       print("|To end this endless loop            type 4  |")
       print("+--------------------------------------------+")
       choice=input(">>>")
       if choice=="1":
              insert()
       elif choice=="2":
              check()
       elif choice=="3":
              view()
       elif choice=="4":
              end()
       else:
              
              print("please enter a valid option(either '1'or'2'or'3'or'4')")
              startscreen()
def end():
       print("end of loop")
       exit()
startscreen()
    
