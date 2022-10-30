#write a program for a csv
#file “people.csv” containing
#name,age,profession of people.
#count and display the number
#of people in the following age
#range (20,30),(31,40),(41,50)
#and above 50.
import csv
def insert():
    f=open("people.csv",'w',newline='')
    uj=csv.writer(f)
    l=["name","age","profession"]
    uj.writerow(l)
    while True:
        a=input("enter the name")
        b=int(input("enter the age"))
        c=input("enter the profession")
        d=[a,b,c]
        uj.writerow(d)
        k=input("enter t to exit any other letter to continue")
        if k=="t":
            break
def vivid():
    z=0
    x=0
    n=0
    m=0
    f=open("people.csv",'r',newline='')
    j=csv.reader(f)
    next(j)
    for i in j:
        if int(i[1])>=20 and int(i[1])<=30:
            z+=1
        if int(i[1])>=31 and int(i[1])<=40:
            x+=1
        if int(i[1])>=41 and int(i[1])<=50:
            n+=1
        if int(i[1])>50:
            m+=1
    print("the number of people in the age group(20-30) is ",z)
    print("the number of people in the age group(31-40) is ",x)
    print("the number of people in the age group(41-50) is ",n)
    print("people whose age is greater than 50 are ",m)
insert()
vivid()
