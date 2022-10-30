f=open("new things.txt",'r')

try:
      while True:
            d=f.read()
            L=d.split()

            for i in L:
                  if i[0]=="i":
                        print(i[::-1],end="\n")
                  else:
                        print(i,end="\n")


                        
            
except:
      f.close()
      print("end of process")


      






