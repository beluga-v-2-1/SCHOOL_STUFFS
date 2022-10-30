#view notepad


def endoffile():
      print("do you want to close the file or continue with the program ?")
      print("type 1 TO CONTINUE ")
      print("type 2 TO CLOSE ")
      new=input(">>>")
      if new=="1":
            startup()
      elif new=="2":
            exit()

      else:
            print(" dude enter a valid number")
            endoffile()
            

def startup():
      
      print("enter the name of the file you are trying to open")
      newest=input(">>>")
      newest+=".txt"
      try:
            
            with open(newest ,'r') as f3:
                  new=f3.read()
                  print(new)
                  endoffile()

      except FileNotFoundError as e:
            
            print(e)
            startup()

startup()
