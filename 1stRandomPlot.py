import matplotlib.pyplot as plt
import numpy as np
import random

k=[]
l=[]

ran=int(random.randrange(0,10,1))
print('ran : ',ran)
x=np.array(random.sample(range(100), ran))

print('x : ',x)

i=0
while i<ran:
    num=10*x[i]+7
    l.append(num)
    i+=1
y=np.array(l)

data = np.vstack([x, y]).T
print (data[:])


plt.xlabel("Avg Pulse")
plt.ylabel("Avg Life")
plt.scatter(x, y,marker='+')

a=np.sum(x)
b=np.sum(y)

p=[]
i=0
while i<ran:
    p.append(x[i]*y[i])
    i+=1
print('x[i]*y[i] :',p)
c=np.sum(p)

i=0
u=[]
while i<ran:
    u.append(x[i]*x[i])
    i+=1
print('x[i]*x[i] :',u)
d=np.sum(u)

print('sum of array xi^2 : ',d)
print('sum of array xi*yi : ',c)
print('sum of array x :',a, '\nsum of array y :',b)

m=a
n=b
v=c
r=d

z=(m*n-ran*v)/(m*m-ran*r)
s=(m*v-n*r)/(m*m-ran*r)

print("z : ",z,"\ns : ",s)
print('formula is : \n')
print('y = ',z,'x + ',s)

plt.plot(x, y, marker='+')
plt.show()