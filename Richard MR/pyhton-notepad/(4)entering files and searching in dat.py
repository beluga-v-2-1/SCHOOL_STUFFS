
import timerbhaimoduleimp as th
import pickle
def entering():
      l=[]
      m=[]
      f=open("binaryfilequestion4.dat",'ab')
      
      a='y'
      while a=='y':
            th.ty("enter roll no")
            h=int(input(">>>"))
            th.ty("enter the name")
            b=input(">>>")
            th.ty('enter the mark')
            c=int(input(">>>"))
            l=[h,b,c]
            pickle.dump(l,f)
            th.ty("do you want to make any changes ? (y/n)")
            a=input(">>>")

            

      f.close()
def search():
      f1=open("binaryfilequestion4.dat",'rb')
      th.ty("enter the name you wanna search?")
      a=input(">>>")
      try:
            while True:
                  k=pickle.load(f1)
                  if k[1]==a:
                        th.ty(k)
      except NameError as e:
            print(e)
            th.ty("there is noone with that name")
            f1.close()

      except EOFError as e:
            f1.close()
            print(e)
            th.ty("process is done")

entering()
search()           
      
