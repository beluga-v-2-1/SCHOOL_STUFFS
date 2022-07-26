



    
curs.execute("select * from employeetest")
table = curs.fetchall()

for x in table:
    print(x)


def addpeople():
    print("thanks for choosing to add new employees")
    print("enter a admission number")
    n1=input()
    print("enter a new name")
    n2=input()
    print("enter a new phoneno")
    n3=input()
    print("enter sex")
    n4=input()
    print("enter a age ")
    n5=input()
    curs.execute("insert into employeetest values('{}','{}','{}','{}','{}')".format(n1,n2,n3,n4,n5))
    curs.execute("select * from employeetest")
    results=curs.fetchall()
    for i in results :
        print(i)             
                 
heppatitis=addpeople()
