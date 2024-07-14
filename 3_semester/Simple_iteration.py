
import numpy as np
from numpy import linalg as LA

N=int(input("N сюды давай:"))
print("A сюдаааа, но только СИММЕТРИЧНУЮ!!!:")
A=[[np.float64(i) for i in input().split()] for _ in range(N) ]
def norm_2(X):
  return ((X.transpose()@X)[0][0])**0.5

q=LA.eig(A)[0]
t=2/(max(q)+min(q))

print("B сюдаааа:")
b=np.array([np.float64(i) for i in input().split()]).reshape(N,1)
X=np.array([0]*N).reshape(N,1)
X_0=X.copy()


eps=10**-5
количество=1
X=X+t*(b-A@X)
AZ=A@(X_0-b)
eps=eps*min(q)**0.5/max(q)**0.5
print(eps)
while(  norm_2((A@X-b)) >eps*norm_2(AZ)):
  количество+=1
  X=X+t*(b-A@X)
print(количество)
print(X)