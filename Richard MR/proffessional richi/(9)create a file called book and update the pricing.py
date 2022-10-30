#write a program to create a
#binary file book with book
#number,name and price . update
#the price of the book using
#given bookname
import pickle
import os
def enters():
    f=open("book.dat",'wb')
    a=int(input("enter the number of books you want to enter"))
    for i in range (a):
        b=int(input("enter the book number"))
        c=input("enter the book name")
        d=int(input("enter the price of book"))
        e=[b,c,d]
        pickle.dump(e,f)
    f.close()
def updates():
    f=open("book.dat",'rb')
    f1=open("book1.dat",'wb')
    k=input("enter the name of the book whose price you want to update")
    l=[]
    try:
        while True:
            g=pickle.load(f)
            if g[1]==k:
                y=input("enter the new price")
                g[2]=y
                pickle.dump(g,f1)
            else:
                pickle.dump(g,f1)     
    except EOFError:
        f.close()
        f1.close()
enters()
updates()
os.remove("book.dat")
os.rename("book1.dat","book.dat")
f=open("book.dat",'rb')
try:
    while True:
        k=pickle.load(f)
        print(k)
except EOFError:
    f.close()
