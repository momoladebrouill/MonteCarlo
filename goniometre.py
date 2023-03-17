from monte_carlo import MonteCarlo
from math import sin,pi

N = 500

# Pour la première expérience :
alpha1 = MonteCarlo(159.45,1,N) * pi / 180
alpha2 = MonteCarlo(118.16,1,N) * pi / 180

deltaa = alpha1 - alpha2
dm = deltaa / 2

p = 1
l_sodium = 589.3e-9
a = p * l_sodium / (2*(dm/2).apply(sin) )

print(f'dm = {dm}rad,\n a = {a}m')

# Pour la deuxième expérience :

alpha1 = MonteCarlo(158.33,1,N) * pi / 180
alpha2 = MonteCarlo(119.66,1,N) * pi / 180

deltaap = alpha1 - alpha2
dmp = deltaap / 2

p = 1
l_verte = 2 * a * (dmp/2).apply(sin)

print(l_verte)
v_att=546.1e-9
print("zscore:", abs(v_att - l_verte.v)/(2*l_verte.u))
