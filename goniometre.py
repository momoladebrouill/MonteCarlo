from monte_carlo import MonteCarlo
from math import sin

N = 500

alpha1 = MonteCarlo(2.78,0.01,N)
alpha2 = MonteCarlo(2.06,0.01,N)

deltaa = alpha1 - alpha2
dm = deltaa / 2

p = 1
l = 589e-9
a = 2 * p * l / (dm/2).apply(sin) 

print(f'dm = {dm}rad,\n a = {a}m')
