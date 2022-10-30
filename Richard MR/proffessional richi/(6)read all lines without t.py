#write a program to remove all
# lines starting with T or t
def randomize():
      try:
            with open("new things.txt",'r') as f:
                  with open("new things2.txt",'w') as f2:
                        x=f.readlines()
                        for i in x:
                              if i[0]=="t" or i[0]=="T":
                                    print("")
                              else:
                                    f2.write(i)                 
            print("the process is done take a look at your file now...")
            with open("new things2.txt",'r') as newfile:
                  newlines=newfile.read()
                  print(newlines)
      except FileNotFoundError as e:
            print(f"{e} so we have decided to make the file")
            print("what would you like to enter onto the file ?")
            choicer=input(">>>")
            with open("new things.txt",'a') as fer:
                  fer.write(choicer)
                  print("we have succesfully created a new file")
                  randomize()
randomize()                  

