#Write a program to count
#and display the number of
#lines,words,vowels and digits
#present in a text file
def newfile():
      print("enter a file name")
      choice=input(">>>")
      a=choice+".txt"
      return a
def printscreen():
      try:
            print("press enter to start")
            print("type end to stop")
            choice=input(">>>")
            if choice == "":
                  linecheck()
            elif choice.lower() == "end":
                  exit()
            else:
                  linecheck()
      except FileNotFoundError as e:
                  
            print(e)
            printscreen()
def linecheck():
      try:
            with open(newfile(),"r") as f:
                  counter=0
                  n=f.readlines()
                  for i in n:
                        counter+=1
                  print(f"the number of lines is {counter}")
                  charecsketch()
      except FileNotFoundError as e:
            print(e)
            printscreen()
def charecsketch():
      try:    
            global x
            with open('student.txt','r') as f:
                  n=f.read()
                  print(f"the number of characters in this file is {len(n)}")
                  printscreen()
      except FileNotFoundError as e:
            print(e)
            printscreen()
printscreen()  
