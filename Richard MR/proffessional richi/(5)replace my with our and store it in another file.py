#write a program to read
#the contents of a textfile
#and modify it by replacing
#the word my with our and
#store it in another file.
with open("new things.txt",'r') as f :
      f1=open("new things200.txt",'w')
      L=[]
      x=f.read()
      n=x.split()
      for i in n:
            if i.lower=="my":
                  i="our"
                  L.append(i)
                  L.append(" ")
            elif i==".":
                  L.append("\n")
            else:
                  L.append(i)
                  L.append(" ")
      f1.writelines(L)
      f1.close()


