#this is a program to convert
#decimal values
#to binary values
def convert():
      L=[]
      aa=input("enter an integer please")
      try:
            a=int(aa)
      except:
            print("enter an integer please")
            convert()
      while a!=0:
            b=a%2
            a=a//2
            L.append(b)

      while L!=[]:
            print(L.pop(),end="")
      print()
convert()
g=input("do you want to continue")
while g in "y,Y":
      convert()
      g=input("do you want to continue")
      
      
exit()
