import numpy as np
N=int(input())
A=np.array([[np.float64(i) for i in input().split() ] for j in range(N)])
Yk=np.array([np.float64(1)]*N).reshape(N,1)
def scalar_mp(X,Y):
  return (X.transpose()@Y)[0][0]

Y=[Yk.copy(),Yk.copy()]
l=[10,0]
while(abs(l[1]-l[0])>0.00001):
  
  Y[0]=Y[1]
  Y[1]=A@Y[1]
  l[0]=l[1]
  l[1]=scalar_mp(Y[1],Y[0])/scalar_mp(Y[0],Y[0])
  Y[1]/=(scalar_mp(Y[1],Y[1]))**0.5
print(l[1]) 
Y=[Yk.copy(),Yk.copy()]
l=[10,0]
B=np.linalg.inv(A)
while(abs(l[1]-l[0])>0.00001):
  
  Y[0]=Y[1]
  Y[1]=B@Y[1]
  l[0]=l[1]
  l[1]=scalar_mp(Y[1],Y[0])/scalar_mp(Y[0],Y[0])
  Y[1]/=(scalar_mp(Y[1],Y[1]))**0.5
  


print(l[1]) 
