import numpy as np
N=int(input())
A=np.array([[np.float64(i) for i in input().split() ] for j in range(N)])
Yk=np.random.randn(N, 1)
def scalar_mp(X,Y):
  return (X.transpose()@Y)[0][0]

for i in range(N):
  Y=[Yk.copy(),Yk.copy()]
  l=[10,0]
  while(abs(l[1]-l[0])>0.0000001):
    Y[0]=Y[1]
    Y[1]=A@Y[1]
    l[0]=l[1]
    l[1]=scalar_mp(Y[1],Y[0])/scalar_mp(Y[0],Y[0])
    #print(Y[1],"ДО:")
    Y[1]/=(scalar_mp(Y[1],Y[1]))**0.5
    #print(Y[1],"что просиходит?")
  print(l[1])  
  
  P=np.eye(N,N)-Y[1]@(Y[1]).transpose()
  
  A=P@A@P
  