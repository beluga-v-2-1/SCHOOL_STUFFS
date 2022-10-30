#write a program to create a
#csv file employ containing
#the following details eno,ename
#designation,phno.The user should
#enter a designation of the employee
#with that designation print the
#employee’s name and phone no
import csv
def add():
    f=open("employ.csv",'w',newline='')
    k=["Eno","Ename","Designation","Phno"]
    writ=csv.writer(f)
    writ.writerow(k)
    while True:
        a=input("enter the Eno")
        b=input("enter the Ename")
        c=input("enter the designation")
        d=input("enter the phone no")
        e=[a,b,c,d]
        writ.writerow(e)
        s=int(input("enter 1 to coninue 2 to exit"))
        if s==2:
            break
def find():
    f=open("employ.csv",'r',newline='')
    z=input("enter the designation to search")
    rr=csv.reader(f)
    for i in rr:
        if i[2]==z:
            print("name : ",i[1])
            print("phone number : ",i[3])
add()
find()
