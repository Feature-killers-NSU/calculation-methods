# Метод Ньютона для нелинейных систем
import numpy as np
import sympy as sp
import sympy.parsing.sympy_parser as prs
# для одномерного случая : f(x)=0,x_n+1=x_n-f(x_n)/f'(x_n)
# для многомерного случая: F(x)=0,F-набор функций(отображение из R^n в  R^n),x_n-уже вектор 
# x_n+1=x_n-F(x_n)*(D(F(x_n)))^-1 

n=int(input())
eps=np.float64(0.001)
x=sp.symbols('x')
for i in range(n):
  expr=input("f(x)=0.Введите n-штук f-ий: ")
  f=prs.parse_expr(expr,transformations="all")

x_0=np.float64(input("Введите начальное приближение: "))
A=[np.float64(0),x_0,x_0+np.float64(10)]
x=sp.symbols('x')
