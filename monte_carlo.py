import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import numpy.random as rd  # sous-module numpy pour générer des tableaux de nbres aléatoire

squared = lambda x:x*x

class Grand:
    def __init__(self, valeur, delta):
        self.v = valeur
        self.d = abs(delta)
        self.u = delta / sqrt(3)

    def __add__(self, other):
        if type(other)==type(self):
            r = Grand(self.v+other.v, 0)
            r.u = sqrt(self.u * self.u + other.u * other.u)
            return r
        elif type(other)==float or type(other)==int:
            r = Grand(self.v+other,0)
            r.u = abs(other) * self.u
            return u
        else:
            raise ArithmeticError

    def __mul__(self, other):
        if type(other) == type(self) : 
            r = Grand(self.v*other.v,self.d)
            r.u = r.v * sqrt(squared(self.u/self.v)+squared(other.u/other.v))
            return r
        else:
            r = Grand(self.v*other,self.d)
            r.u = abs(other)*self.u
            return r

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

    def __sub__(self,other):
        if type(self)==type(other):
            r = MonteCarlo(self.b,other.v,self.d,1)
            r.sim = self.sim - other.sim
            return r
        else:
            return MonteCarlo(self.v-other,self.d,self.n)
    
    @property()
    def v(self):
        return np.average(self.sim)
    
    @property()
    def u(self):
        return np.std(self.sim,ddof=1)
    
    def __repr__(self):
        return f"{round(self.v,10)}±{round(self.u,11)"



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
T_sim = t1_sim - t2_sim
print(
      "Résultat obtenu par simulation Monte Carlo : T ",
      T_sim,
      "s"
)
