import numpy as np
import matplotlib.pyplot as pyplot

def Euclid_norm(x):
    norm = 0
    for i in x:
        norm += i**2
    return np.sqrt(norm)

def scalar(x, y):
    sc = 0
    for i in range(len(x)):
        sc += x[i]*y[i]
    return sc

def max_eigenv(g_i, acc_i):
    accuracy = [0.000001,0.0000001,0.00000001]
    grid = [10,20,40]
    n=grid[g_i]
    delta=accuracy[acc_i]
    
    a,b = 1,1.2

    h = 1/n

    Y = np.zeros((n+1,n+1))
    Y_n = np.zeros((n+1, n+1))

    #заполняю матрицу(зависит от области)
    for i in range (1,n):
        for j in range(1,int(n/2)):
            Y[j][i] = 1

    for i in range(int(n/2),n):
        for j in range(i,n):
            Y[i][j] = 1

    #инициализация Y1
    for i in range(1,n):
        for j in range(1,n):
            Y_n[i][j] = -1*(a/h**2)*(Y[i-1][j] - 2*Y[i][j] + Y[i+1][j])\
            -(b/h**2)*(Y[i][j-1]-2*Y[i][j]+Y[i][j+1])

    #лямбда на первой итерации
    lambda_max_n = scalar(Y_n.reshape(-1)/ Euclid_norm(Y.reshape(-1)), Y.reshape(-1)/Euclid_norm(Y.reshape(-1)))
    iter = 1
    # вычисление максимального собственного значения A
    while True:
        iter += 1
        lambda_max_0 = lambda_max_n

        Y = Y_n.copy()/Euclid_norm(Y.reshape(-1))

        for j in range(1, n):
            for i in range(1, n):
                Y_n[j][i] = -1*(a/h**2)*(Y[j][i-1] - 2*Y[j][i] + Y[j][i+1]) -\
                (b/h**2)*(Y[j-1][i] - 2*Y[j][i] + Y[j+1][i])

        lambda_max_n = scalar(Y_n.reshape(-1)/\
        Euclid_norm(Y.reshape(-1)), Y.reshape(-1)/Euclid_norm(Y.reshape(-1)))

        if np.abs(lambda_max_n - lambda_max_0)/lambda_max_0 < delta:
            break
    return [lambda_max_n, iter]

# ммаксимальные числа
print("максимальные числа А:")
for i in range(3):
    for j in range(3):
        KKK=max_eigenv(i,j)
        print("n=grid[",i,"]","delta=accuracy[",j,"]:","c-б число:",KKK[0],"кол-во итераций:",KKK[1])

def min_eigenv(g_i,acc_i):
 
 accuracy = [0.000001,0.0000001,0.00000001]
 grid = [10,20,40]

 n = grid[g_i]
 delta = accuracy[acc_i]

 #самое точное значение для данного h
 lambda_max_n = max_eigenv(g_i,2)[0]
 a,b = 1.1,0.8
 h = 1/n
 Y = np.zeros((n+1,n+1))
 Y_n = np.zeros((n+1, n+1))
 #заполняю матрицу(зависит от области)
 for i in range (1,n):
     for j in range(1,int(n/2)):
            Y[j][i] = 1

 for i in range(int(n/2)+1,n):
     for j in range(i,n):
            Y[i][j] = 1
 Psi = Y.copy()
 Psi_n = Psi.copy()
 # Psi - нач
 for j in range(1, n):
     for i in range(1, n):
         Psi_n[j][i] = lambda_max_n*Psi[j][i] + \
         (a/h**2)*(Psi[j][i-1] - 2*Psi[j][i] + Psi[j][i+1]) + \
         (b/h**2)*(Psi[j-1][i] - 2*Psi[j][i] + Psi[j+1][i])

 lambda_max_B_n = scalar(Psi_n.reshape(-1)/Euclid_norm(Psi.reshape(-1)), \
                     Psi.reshape(-1)/Euclid_norm(Psi.reshape(-1)))

 iter = 1
 #вычисление максимального собственного значения B
 while True:
     iter += 1
     lambda_max_B_0 = lambda_max_B_n

     Psi = Psi_n.copy()/Euclid_norm(Psi.reshape(-1))

     for j in range(1, n):
         for i in range(1, n):
             Psi_n[j][i] = lambda_max_n*Psi[j][i] + \
             (a/h**2)*(Psi[j][i-1] - 2*Psi[j][i] + Psi[j][i+1]) + \
             (b/h**2)*(Psi[j-1][i] - 2*Psi[j][i] + Psi[j+1][i])

     lambda_max_B_n = scalar(Psi_n.reshape(-1)/Euclid_norm(Psi.reshape(-1)), \
                         Psi.reshape(-1)/Euclid_norm(Psi.reshape(-1)))

     if np.abs(lambda_max_B_n - lambda_max_B_0)/lambda_max_B_0 < delta:
         break
 return lambda_max_n - lambda_max_B_n,iter





# миниальное собственное значение А
print("минимальные числа А:")
for i in range(3):
    for j in range(3):
        KKK=min_eigenv(i,j)
        print("n=grid[",i,"]","delta=accuracy[",j,"]:","c-б число:",KKK[0],"кол-во итераций:",KKK[1])
