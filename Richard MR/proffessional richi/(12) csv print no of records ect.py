#Program to create a csv
#file and find the number
#of records and also print
#all the records
import csv
def enter():
    f=open("sag.csv",'w',newline='')
    g=["empname","empno","salary"]
    v=csv.writer(f)
    v.writerow(g)
    while True:
        a=input("enter the employee name")
        b=input("enter the employee number ")
        c=input("enter the salary ")
        d=[a,b,c]
        v.writerow(d)
        cc=int(input("enter 1 to coninue 2 to exit"))
        if cc==2:   
            break
    f.close()
def count():
    f=open("sag.csv",'r',newline='')
    t=0
    o=csv.reader(f)
    for i in o:
        print(i[0],i[1],i[2],sep="\t")
    f.seek(0)
    next(o)
    for i in o:
        t+=1
    print("the number of records are",t)
    
enter()
count()
