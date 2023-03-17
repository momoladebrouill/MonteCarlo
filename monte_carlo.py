import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import numpy.random as rd  

grec ={"a":"α",
       "b":"β", 
       "g":"γ", 
       "D":"Δ",
       "d":"δ",
       "e":"ε",
       "z":"ζ",
       "h":"η",
       "T":"Θ",
       "t":"θ",
       "i":"ι", 
       "k":"κ", 
       "L":"Λ",
       "l":"λ",
       "m":"μ",
       "n":"ν", 
       "Xi":"Ξ", 
       "xi":"ξ",
       "o":"ο", 
       "P":"Π",
       "p":"π",
       "r":"ρ", 
       "S":"Σ",
       "s":"σ",
       "t":"τ", 
       "y":"υ", 
       "F":"Φ",
       "f":"φ",
       "x":"χ", 
       "Psi":"Ψ", 
       "psi":"ψ", 
       "O":"Ω",
       "omega":"ω"}

squ = lambda x : x * x
is_number = lambda x: type(x) == int or type(x) == float
u_prod = lambda a,b,res : res.v * sqrt(squ(a.u/a.v)+squ(b.u/b.v))
u_som = lambda a,b,res : sqrt(squ(a.u) + squ(b.u))

class Env :
    def __init__(self, N = 1000, prec = 3):
        self.N=N
        self.prec=prec

class Grand:

    def __init__(self, valeur, delta, env=Env()):
        self.v = valeur
        self.d = abs(delta)
        self.u = self.d / sqrt(3)
        self.env = env

    def __abs__(self):
        return Grand(abs(self.v),self.d)
    
    def evaluate(self,other,fun,ufun):
        if type(self)==type(other):
            r = Grand(fun(self.v,other.v),self.d,self.env)
            r.u = ufun(self,other,r)
        elif is_number(other):
            r = Grand(fun(self.v,other),self.d,self.env)
            r.u = self.u
        else :
            raise ArtitmeticError
        return r

    def apply(self,fun):
        g = Grand(fun(self.v),1,env=self.env)
        g.u = self.u
        return g
    
    def __add__(self, other):
        return self.evaluate(other,lambda x,y : x+y,u_som)

    def __sub__(self, other):
        return self.evaluate(other,lambda x,y : x-y,u_som)
    
    def __mul__(self, other):
        return self.evaluate(other,lambda x,y : x*y,u_prod)
    
    def __truediv__(self, other):
        return self.evaluate(other,lambda x,y : x/y,u_prod)
    
    def __rsub__(self, other):
        return self.evaluate(other,lambda x,y : y-x,u_som)

    def __rtruediv__(self, other):
        return self.evaluate(other,lambda x,y : y/x,u_prod)
    
    def __repr__(self):
        return f"{round(self.v,self.env.prec)}±{round(self.u,self.env.prec)}"

    def generate(self,n):
        self.sim = self.v + rd.uniform(-self.d,self.d,n)

    __rmul__=__mul__
    __radd__=__add__

class MonteCarlo:
    
    def __init__(self,v,d,env = Env()):
        self.truev = v
        self.d = d
        self.env = env
        self.sim = v + rd.uniform(-d,d,env.N)

    def montecarlotte(self,other, fun):
        if type(self)==type(other):
            r = MonteCarlo(fun(self.truev,other.truev),self.d,self.env)
            r.sim = [fun(x,y) for x,y in zip(self.sim,other.sim)]
            return r
        elif is_number(other):
            return self.apply(lambda x : fun(x,other))
        else:
            raise ArithmeticError

    def apply(self,fun):
        r = MonteCarlo(fun(self.truev),self.d,self.env)
        r.sim = [fun(x) for x in self.sim]
        return r

    def __add__(self,other):
        return self.montecarlotte(other,(lambda x,y : x + y))
    
    def __mul__(self,other):
        return self.montecarlotte(other,(lambda x,y : x * y))
    
    def __sub__(self,other):
        return self.montecarlotte(other,(lambda x,y : x - y))
    
    def __truediv__(self,other):
        return self.montecarlotte(other,(lambda x,y : x / y))
    
    def __rsub__(self,other):
        return self.montecarlotte(other,(lambda x,y : y - x))
    
    def __rtruediv__(self,other):
        return self.montecarlotte(other,(lambda x,y : y / x))

    __radd__=__add__
    __rmul__=__mul__
        
    @property
    def v(self):
        return np.average(self.sim)
    
    @property
    def u(self):
        return np.std(self.sim,ddof=1)
    
    def __repr__(self):
        return f"{round(self.v,self.env.prec)}±{round(self.u,self.env.prec)}"
