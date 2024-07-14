import numpy as np
import sympy as  sp
import sympy.parsing.sympy_parser as prs

#Ньютон

expr=input("f(x)=0.Введите f: ")
eps=np.float64(input("Введите точность корня: "))
x_0=np.float64(input("Введите начальное приближение: "))
A=[np.float64(0),x_0,x_0+np.float64(10)]
x=sp.symbols('x')
f=prs.parse_expr(expr,transformations="all")
d_f=sp.diff(f,x)

kk=0
while(abs(A[2]-A[1])>eps):
  kk+=1
  A[0]=A[1]
  A[1]=A[2]
  A[2]=A[1]-f.evalf(subs={x: A[1]})/d_f.evalf(subs={x: A[1]})

print("Корень: ", A[1])    
print("Кратность: ", round((A[1]-A[0])/(-A[2]+2*A[1]-A[0])))
print(kk)


#Метод Хорд
'''
expr=input("g(x)=0.Введите g: ")
eps=np.float64(input("Введите точность корня: "))
a,b=[np.float64(i) for i in input("Введите a,b: ").split()]
A=[a-np.float64(10),a]
x=sp.symbols('x')
f=prs.parse_expr(expr,transformations="all")
d_f=sp.diff(f,x)
kk=0
while(abs(A[0]-A[1])>eps):
  kk+=1
  A[0]=A[1]
  A[1]=b-f.evalf(subs={x:b})*(b-A[0])/(f.evalf(subs={x:b})-f.evalf(subs={x:A[0]}))

print("Корень:", A[1]) 
print(kk)
'''















