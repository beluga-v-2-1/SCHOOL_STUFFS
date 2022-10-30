#Write a program to create
#a binary file with roll
#number,name and mark of
#the students and to search
#for a particular student
#using the name and display
#the record.
import pickle
def enter():
    f=open("jack.dat",'wb')
    a=int(input("enter the number of record you want to enter"))
    for i in range (a):
        b=int(input("enter the roll number"))
        c=input("enter the name")
        d=int(input("enter the mark"))
        e=[b,c,d]
        pickle.dump(e,f)
    f.close()
def search():
    while True:
        n=input("enter the name to search")
        f=open("jack.dat",'rb')
        p=0
        try:
            while True:
                k=pickle.load(f)
                if k[1]==n:
                    print("The roll number of the student is ",k[0])
                    print("The name of the student is ",k[1])
                    print("The mark of the student is ",k[2])    
                    p=p+1     
        except EOFError:
            f.close()
        if p==0:
            print("no student with such name exist")
        z=int(input("if you do not want to continue press 1"))
        if z==1:
            break  
enter()
search()
