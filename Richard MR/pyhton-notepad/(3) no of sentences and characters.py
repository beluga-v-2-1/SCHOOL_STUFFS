
      
def inputs():
      print("please enter the name of the file this is regarding")
      y=input(">>>")
      
      return y
      
def printscreen():
      print("To find the number of characters in a file    type 1")
      print("To find the number of lines in a file         type 2")
      print("To exit this program                          type 3")
      choice=input(">>>")
      if choice == "1":
            charecsketch()
      elif choice == "2":
            linecheck()

      elif choice == "3":
            c=1
            exit()

      else :
            print("please enter a valid option")
            printscreen() 
def linecheck():
      with open(x,"r") as f:
            counter=0
            n=f.readlines()
            for i in n:
                  counter+=1
            print(f"the number of lines is {counter}")      
            

def charecsketch():
            

      global x
            
      with open(x,'r') as f:
            n=f.read()
            print(f"the number of characters in this file is {len(n)}")

c=0
x=inputs()
while c==0:
      
      printscreen()
      
           


