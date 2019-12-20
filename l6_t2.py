import numpy as np
import matplotlib.pyplot as plt

def sqlist(i):
    o=np.linspace(8.,9.,num=len(i))
    for x in range(0,len(i)):
            o[x]=i[x]**2
    return o
def sinlist(i):
    o=np.linspace(8.,9.,num=len(i))
    for x in range(0,len(i)):
        o[x]=np.sin(i[x])
    return o

#l=[1,2,3,4,5,6,7,8,9]
l=np.linspace(0,100,num=1000)
squarelist=sqlist(l)
sinl=sinlist(l)

plt.plot(l,squarelist)
plt.plot(l,sinl)
plt.show()