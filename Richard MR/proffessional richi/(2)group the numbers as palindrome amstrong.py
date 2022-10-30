# write a program to input ‘n’ numbers
#and group the numbers in angstrom
#number,palindrome number,
#nd other numbers.

a=int(input("enter the number of numbers you want to enter "))
f=[]
for i in range (0,a):
    b=int(input("enter the number"))
    f.append(b)
    
g=[]   
for i in f:
    c=str(i)
    if c==c[::-1]:
        g.append(int(c))
print("the palindrome numbers entered are :  ",g)
l=[]
for i in f:
    v=[]
    b=i
    string=str(i)
    length=len(string)
    while i!=0:
        z=i%10
        v.append(z)
        i=i//10
    p=0
    for j in v:
        p=p+(j**length)
    if p==b:
        l.append(p)
        
print("the angstrom numbers are : ",l)
k=[]
for i in f:
    if i not in g and i not in l:
        k.append(i)
print("the other numbers are ",k)        
