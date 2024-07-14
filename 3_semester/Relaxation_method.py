import numpy as np
N=int(input())
A=np.array([[ np.float64(i) for i in input().split()] for _ in range(N)]).reshape(N,N)
b=np.array([ np.float64(i) for i in input().split()]).reshape(N,1)
x1 = np.random.randn(N, 1).astype(np.float64())
x2=10*x1
#x=np.array([1,2]).reshape(2,1)



def iterations_i_solve(A,x,b):
  for i in range(N):
   x[i][0]-=((A[i]@x)[0]-b[i][0])/A[i][i];
  return x
k=0
def iterations_k_solve(A,x1,x2,b):
  global k
  while(((A@(x1-x2)).transpose()@(x1-x2))[0][0]**0.5>0.000001):
    k+=1
    x2=x1.copy()
    x1=iterations_i_solve(A,x1,b)
  return x1
print(A@iterations_k_solve(A,x1,x2,b))
print(k)