import numpy as np
import sympy as sp
import sympy.parsing.sympy_parser as prs


sp.init_printing(use_unicode=False, wrap_line=False)



def mul(x,dotes,k):
  P=1
  
  for i in range(len(dotes)):
    if(i!=k):
      P*=(x-dotes[i])
  return P    
'''  
x =sp.Symbol('x')
print((sp.integrate(mul(x,[2,3],-1),x)).evalf(subs={x:2}))
'''



def Quadratura_Newton_Cotexa(a,b,expr,n):
  x=sp.Symbol('x')
  f=prs.parse_expr(expr,transformations="all")
  dx=(b-a)/n
  dotes=[(a+dx*i) for i in range(n)]
  B=0

  for k in range(n):
    B+=sp.integrate(mul(x,dotes,k),(x,a,b))*f.evalf(subs={x:dotes[k]})/mul(dotes[k],dotes,k)
    
  return B

#expr=input("f(x): ")

expr="sin(x)" 
pi=3.1415926535
I_1=Quadratura_Newton_Cotexa(0,sp.pi,expr,4)
I_2=Quadratura_Newton_Cotexa(0,sp.pi,expr,8)
I_3=Quadratura_Newton_Cotexa(0,sp.pi,expr,16)
print(sp.log((I_1-I_2)/(I_2-I_3))/sp.log(2))


