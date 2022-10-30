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
