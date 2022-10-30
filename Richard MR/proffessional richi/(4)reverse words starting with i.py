#AIM : write a program to
#insert a string in a text
#file , read the file and
#display the contents by
#reversing the word which
#are starting with i or I

def mains():
    f=open("wizzard.txt",'w')
    a=input("enter the string")
    f.write(a+"\n")
    f.close()
    g=open("wizzard.txt",'r')
    t=g.read()
    k=t.split()
    for i in k:
        if i[0] in "iI":
            i=i[::-1]
        print(i,end=" ")
    g.close()
mains()
