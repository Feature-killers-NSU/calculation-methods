import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 1.2

def norm(x,n):
    h = 1/n
    norm = 0
    for i in x:
        norm += i**2
    return np.sqrt(norm)*h

def sc(x, y):
    sc = 0
    for i in range(len(x)):
        sc += x[i]*y[i]
    return sc

def func_f(y,x):
    return 0.2*np.exp(x)*np.cos(y)

def func_phi(y,x):
    return np.exp(x)*np.cos(y)

def start_matrix(n):
    Y = np.zeros((n+1,n+1))
    h = 1/n
    #заполняю матрицу(зависит от области)
    for i in range(1,int(n/2)):
      for j in range (1,n):
            Y[i][j] = 1

    
    for i in range(int(n/2),n):
        for j in range(i,n):
            Y[i][j] = 1

    
    for j in range(1,n):
        Y[0][j] = func_phi(0,j*h)

    for i in range(n):
        Y[i][n] = func_phi(i*h,1)

    for i in range(int(n/2)+1):
        Y[i][0] = func_phi(i*h,0)
    
    for j in range(int(n/2)):
        Y[int(n/2)][j] = func_phi(int(n/2)*h,j*h)

    for i in range(int(n/2),n+1):
        Y[i][i] = func_phi(i*h,i*h)
    
    return Y

def mult_by_A(Y,n):
    h = 1/n
    Res = np.zeros((n+1,n+1))
    for i in range(1,int(n/2)):
       for j in range (1,n):
            Res[i][j] = -1*(b/h**2)*(Y[i-1][j]-2*Y[i][j]+Y[i+1][j]) - (a/h**2)*(Y[i][j-1]-2*Y[i][j]+Y[i][j+1])
    for i in range(int(n/2),n):
        for j in range(i,n):
            Res[i][j] = -1*(b/h**2)*(Y[i-1][j]-2*Y[i][j]+Y[i+1][j]) - (a/h**2)*(Y[i][j-1]-2*Y[i][j]+Y[i][j+1])
    return Res

def init_F(n):
    h = 1/n
    F = np.zeros((n+1, n+1))

    for i in range(1,int(n/2)):
       for j in range (1,n):
            F[i][j] = func_f(h*i,h*j)

    for i in range(int(n/2),n):
        for j in range(i,n):
            F[i][j] = func_f(h*i,h*j)
         
    return F

def init_phi(n):
    h = 1/n
    phi = np.zeros((n+1, n+1))

    for i in range(1,int(n/2)):
       for j in range (1,n):
            phi[i][j] = func_phi(h*i,h*j)

    for i in range(int(n/2),n):
        for j in range(i,n):
            phi[i][j] = func_phi(h*i,h*j)

    for j in range(1,n):
        phi[0][j] = func_phi(0,j*h)

    for i in range(n):
        phi[i][n] = func_phi(i*h,1)

    for i in range(int(n/2)+1):
        phi[i][0] = func_phi(i*h,0)
    
    for j in range(int(n/2)):
        phi[int(n/2)][j] = func_phi(int(n/2)*h,j*h)

    for i in range(int(n/2),n+1):
        phi[i][i] = func_phi(i*h,i*h)

    return phi


def solve(n, delta):
    Y_n = np.zeros((n+1,n+1))
    Y = start_matrix(n)
    F = init_F(n)
    phi = init_phi(n)

    R = mult_by_A(Y,n) - F
    tau_k = sc(mult_by_A(R,n).reshape(-1), R.reshape(-1)) / sc(mult_by_A(R,n).reshape(-1),mult_by_A(R,n).reshape(-1) )

    Y_n = Y - tau_k*R #Y1
    iter = 1

    while norm(((mult_by_A(Y_n,n)-F)-R).reshape(-1),n) > delta :

        Y = Y_n.copy()

        iter += 1

        R = mult_by_A(Y,n) - F #невязка на данном шаге
        tau_k = sc(mult_by_A(R,n).reshape(-1), R.reshape(-1)) / sc(mult_by_A(R,n).reshape(-1),mult_by_A(R,n).reshape(-1) )

        Y_n = Y - tau_k*(mult_by_A(Y,n)-F)

    epsilon = norm((Y_n - phi).reshape(-1),n)
    return [epsilon, iter]


accuracy = [10**(-6),10**(-7),10**(-8)]
grid = [10,20,40]



for n in grid:
  for delta in accuracy:
     print(solve(n,delta))
'''     
def stsart_matrix(n):
    Y = np.zeros((n+1,n+1))
    h = 1/n
    #заполняю матрицу(зависит от области)
    for i in range(1,int(n/2)):
      for j in range (1,n):
            Y[i][j] = 1

    
    for i in range(int(n/2),n):
        for j in range(i,n):
            Y[i][j] = 1

    
    for j in range(1,n):
        Y[0][j] = 2

    for i in range(n):
        Y[i][n] = 2

    for i in range(int(n/2)+1):
        Y[i][0] = 22
    
    for j in range(int(n/2)):
        Y[int(n/2)][j] = 2
    for i in range(int(n/2),n+1):
        Y[i][i] = 2
    
    return Y
  
print(stsart_matrix(10))
'''