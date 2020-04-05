# code by wickenchen

import numpy as np
import matplotlib.pyplot as plt

"""==========input file.txt=========="""

f=open(r"train.txt","r")
lines=f.readlines()
datalist=[]
label=[]
xp=[]
yp=[]
xn=[]
yn=[]
tw=[]
label=[]
for line in lines:
    line_split=line.split(' ')
    #print(line_split)
    #
    #print(label)
    datalist.append([1,float(line_split[0]),float(line_split[1])])
    #print(datalist)
    if line_split[2][0]=='+':
        label.append(1)
        xp.append(float(line_split[0]))
        yp.append(float(line_split[1]))
    else:
        label.append(-1)
        xn.append(float(line_split[0]))
        yn.append(float(line_split[1]))


"""==========main code of computing=========="""

w=np.matrix([1,1,1])

tw=w.T

label=np.mat(label).T

n,m=np.shape(datalist)
#print(n)
#print(datalist)
#print(tw)

while 1:    
    flag=0
    for i in range(n):
        if np.sign(np.dot(datalist[i],tw))!=label[i]:
            tw=tw+np.mat(label[i]*datalist[i]).T
            flag=1
    if flag==0: 
        break

"""==========output pic=========="""

xline1=-100
yline1=float((0-tw[0][0]-tw[1][0]*xline1)/tw[2][0])

xline2=100
yline2=float((0-tw[0][0]-tw[1][0]*xline2)/tw[2][0])

plt.scatter(xp,yp,marker='o',c='',edgecolors='b')
plt.scatter(xn,yn,marker='x',c='r')
plt.plot([xline1,xline2],[yline1,yline2],c='k')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()



