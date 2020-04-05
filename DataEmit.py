# code by wickenchen

import re
import random

f=open("train.txt","w")

temp=input("")

string=temp

filterdata=re.findall(r"\-?\d+\.?\d*",string)

filternumber=[int(x) for x in filterdata]

[w0,w1,w2,m,n]=filternumber

M=0
N=0
f.seek(0,0)
while M<m or N<n:
    x2=random.uniform(-100,100)
    x1=random.uniform(-100,100)
    flag=w1*x1+w2*x2+w0
    if(flag>0 and M<m):
        label='+'
        M+=1
        f.write(str(x1))
        f.write(" ")
        f.write(str(x2))
        f.write(" ")
        f.write(label)
        f.write("\n")
        '''print(x1,x2,label)'''
    elif(flag<0 and N<n):
        label='-'
        N+=1
        f.write(str(x1))
        f.write(" ")
        f.write(str(x2))
        f.write(" ")
        f.write(label)
        f.write("\n")
        '''print(x1,x2,label)'''
f.close()
    





    
