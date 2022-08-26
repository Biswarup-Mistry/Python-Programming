import matplotlib.pyplot as plt
import numpy as np
import random

k=[]
l=[]

ran=int(random.randrange(0,10,1))

#ran=random.sample(range(10),1)
print('ran : ',ran)

x=np.array(random.sample(range(100), ran))
y=np.array(random.sample(range(100), ran))
print('x : ',x)
print('y : ',y)


plt.scatter(x, y)
plt.show()

data = np.vstack([x, y]).T
print (data[:])


plt.xlabel("Avg Pulse")
plt.ylabel("Avg Life")
plt.scatter(x, y,marker='+')

plt.plot(x, y, marker='+')
plt.show()