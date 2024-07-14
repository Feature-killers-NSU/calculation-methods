import numpy as np
import sympy as sp
import sympy.parsing.sympy_parser as prs



expr=input("f(x): ")

a=[np.float64(i) for i in input().split()]
x=sp.symbols('x')
f=prs.parse_expr(expr,transformations="all")
#quadratura Gaussa(3 узла)
print("Квадратура Гаусса:")
print((a[1]-a[0])*(4/9*f.evalf(subs={x:(a[1]+a[0])/2})+5/18*(f.evalf(subs={x:(a[0]+a[1])/2+1/2*(3/5)**0.5*(a[1]-a[0])})+f.evalf(subs={x:(a[0]+a[1])/2-1/2*(3/5)**0.5*(a[1]-a[0])}))))
#trapecia
print("Трапеция:")
print((a[1]-a[0])*(f.evalf(subs={x:a[0]})+f.evalf(subs={x:a[1]}))/2)


