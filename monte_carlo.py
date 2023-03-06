import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import numpy.random as rd  

squ = lambda x : x * x
is_number = lambda x: type(x) == int or type(x) == float
u_prod = lambda a,b,res : res.v * sqrt(squ(a.u/a.v)+squ(b.u/b.v))
u_som = lambda a,b,res : sqrt(squ(a.u) + squ(b.u))
class Grand:

    def __init__(self, valeur, delta):
        self.v = valeur
        self.d = abs(delta)
        self.u = delta / sqrt(3)

    def __abs__(self):
        return Grand(abs(self.v),self.d)

    def evaluate(self,other,fun,ufun):
        if type(other) == type(self):
            r = Grand(fun(self.v,other.v),self.d)
        elif is_number(other):
            r = Grand(fun(self.v,other.v),self.d)
            other.u = 0
        else:
            raise ArithmeticError
        r.u = ufun(self,other,r)
        return r
    
    def __add__(self, other):
        return self.evaluate(other,lambda x,y : x+y,u_som)

    def __sub__(self, other):
        return self.evaluate(other,lambda x,y : x-y,u_som)
    
    def __mul__(self, other):
        return self.evaluate(other,lambda x,y : x*y,u_prod)
    
    def __div__(self, other):
        return self.evaluate(other,lambda x,y : x/y,u_prod)

    def __repr__(self):
        return f"{round(self.v,10)}±{round(self.u,10)}"

    def generate(self,n):
        self.sim = self.v + rd.uniform(-self.d,self.d,n)

    __rmul__=__mul__
    __radd__=__add__

class MonteCarlo:
    def __init__(self,v,d,n):
        self.truev = v
        self.d = d
        self.n = n
        self.sim = self.truev+rd.uniform(-d,d,n)

    def montecarlotte(self,other, fun):
        if type(self)==type(other):
            r = MonteCarlo(fun(self.truev,other.truev),self.d,1)
            r.sim = fun(self.sim, other.sim)
            return r
        elif is_number(other):
            return MonteCarlo(fun(self.truev,other),self.d,self.n)
        else:
            raise ArithmeticError

    def __add__(self,other):
        return self.montecarlotte(other,(lambda x,y : x + y))
    
    def __sub__(self,other):
        return self.montecarlotte(other,(lambda x,y : x - y))
    
    def __mul__(self,other):
        return self.montecarlotte(other,(lambda x,y : x * y))
    
    def __div__(self,other):
        return self.montecarlotte(other,(lambda x,y : x / y))


    __radd__=__add__
    __rsub__=__sub__
    __rdiv__=__div__
    __rmul__=__mul__
    
    @property
    def v(self):
        return np.average(self.sim)
    
    @property
    def u(self):
        return np.std(self.sim,ddof=1)
    
    def __repr__(self):
        return f"{round(self.v,10)}±{round(self.u,11)}"



N = 10000  # nombre de simulations

# Pour T ----------------------------------
print("Pour T:------")
# intervalles de mesure delta(l'incertitude-type associée est obtenue en divisant cet intervalle par racine de 3)
t1 = Grand(0.0,.2e-6)
t2 = Grand(25e-6,0.12e-6)
T = t2 + (-1*t1)
print(
    "Résultat obtenu par les formules : T = ",
    T,
    "s"
)
t1_sim = MonteCarlo(t1.v,t1.d,N)
t2_sim = MonteCarlo(t2.v,t2.d,N)
T_sim = t2_sim - t1_sim - t2_sim+t1_sim*2
print(
      "Résultat obtenu par simulation Monte Carlo : T ",
      T_sim,
      "s"
)
