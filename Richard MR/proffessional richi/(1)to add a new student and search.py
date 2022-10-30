#AIM: write a  program to add a new
#student (admission number ,name ,mark)
#search for a student and
#display the student details

l=[(10,"sooraj",89),(11,"vishnu",92),(12,"neeraj",98)]
a=0
def app(s):
    h=0
    global a
    print("enter 1 to add a student")
    print( "enter 2 to search a student")
    print("enter 3 to display the details")
    a=int(input())
    if a==1:
        a=int(input("enter the admission number"))
        b=input("enter a name")
        c=int(input("enter the mark"))
        d=(a,b,c)
        s.append(d)
    elif a==2:
        k=input("enter the name you want to search")
        for i in s:
             if i[1]==k:
                 h=i
                 print(h)
        if h==0:
            print("does not exist")
    elif a==3:
        for i in s:
            print("admisiion number-",i[0])
            print("name of student-",i[1])
            print("mark of student-",i[2])
app(l)
while a!=0:
    app(l)



