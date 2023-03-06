import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import numpy.random as rd  # sous-module numpy pour générer des tableaux de nbres aléatoire

N = 10000  # nombre de simulations

# Pour T ----------------------------------
print("Pour T:------")
# intervalles de mesure delta(l'incertitude-type associée est obtenue en divisant cet intervalle par racine de 3)
t1 = 0.0000
delta_t1 = 0.2e-6

t2 = 25e-6
delta_t2 = 0.12e-6

## Calcul des incertitudes approchées via les formules
ut1_calc = delta_t1 / sqrt(3)
ut2_calc = delta_t2 / sqrt(3)
uT_calc = sqrt(ut1_calc**2 + ut2_calc**2)
T = t2 - t1
print(
    "Résultat obtenu par les formules : T = ",
    round(T, 10),
    "+/-",
    round(uT_calc, 10),
    "s"
)

## Calcul des grandeurs simulées par Monte Carlo

t1_sim = t1 + rd.uniform(
    -delta_t1, +delta_t1, N
)  # tableau de N valeurs aléatoires de t1

t2_sim = t2 + rd.uniform(
    -delta_t2, +delta_t2, N
)  # tableau de N valeurs aléatoires de t2

T_sim = t2_sim - t1_sim
T_MC = np.average(T_sim)
uT_MC = np.std(T_sim, ddof=1)

print(
    "Résultat obtenu par simulation Monte Carlo : T ",
    round(T_MC, 10),
    "+/-",
    round(uT_MC, 11),
    "s",
)

#Pour lambda --------------------------------------------------
print("Pour \u03BB:------")
# intervalles de mesure delta(l'incertitude-type associée est obtenue en divisant cet intervalle par racine de 3)
x1 = 14.9e-2
delta_x1 = 1e-3

x2 = 23.8e-2
delta_x2 = 1e-3

## Calcul des incertitudes approchées via les formules
ux1_calc = delta_x1 / sqrt(3)
ux2_calc = delta_x2 / sqrt(3)
uL_calc = sqrt(ut2_calc**2 + ux2_calc**2)/10
L = (x2 - x1)/10
print(
    "Résultat obtenu par les formules : \u03BB = ",
    round(L, 10),
    "+/-",
    round(uL_calc, 10),
    "m"
)

## Calcul des grandeurs simulées par Monte Carlo

x1_sim = x1 + rd.uniform(
    -delta_x1, +delta_x1, N
)  # tableau de N valeurs aléatoires de t1

x2_sim = x2 + rd.uniform(
    -delta_x2, +delta_x2, N
)  # tableau de N valeurs aléatoires de t2

L_sim = (x2_sim - x1_sim)/10
L_MC = np.average(L_sim)
uL_MC = np.std(L_sim, ddof=1)

print(
    "Résultat obtenu par simulation Monte Carlo : \u03BB ",
    round(L_MC, 10),
    "+/-",
    round(uL_MC, 11),
    "m",
)

#Pour c --------------------------------------------------
print("Pour c:------")

## Calcul des incertitudes approchées via les formules
C = L / T
uC_calc = C * sqrt(uL_calc*uL_calc/(L*L)+uT_calc*uT_calc/(T*T))

print(
    "Résultat obtenu par les formules : c = ",
    round(C, 10),
    "+/-",
    round(uC_calc, 10),
    "m"
)

## Calcul des grandeurs simulées par Monte Carlo

C_sim = L_sim/T_sim
C_MC = np.average(C_sim)
uC_MC = np.std(C_sim, ddof=1)

print(
    "Résultat obtenu par simulation Monte Carlo : \u03BB ",
    round(C_MC, 10),
    "+/-",
    round(uC_MC, 11),
    "m",
)


# T
plt.subplot(131)
plt.hist(t1_sim, bins="rice", label="Histogramme de t1_sim")
plt.legend()

plt.subplot(132)
plt.hist(t2_sim, bins="rice", label="Histogramme de t2_sim")
plt.legend()
plt.subplot(133)
plt.hist(T_sim, bins="rice", label="Histogramme de T_sim")
plt.legend()
# L
plt.subplot(231)
plt.hist(x1_sim, bins="rice", label="Histogramme de x1_sim")
plt.legend()
plt.subplot(232)
plt.hist(x2_sim, bins="rice", label="Histogramme de x2_sim")
plt.legend()
plt.subplot(233)
plt.hist(T_sim, bins="rice", label="Histogramme de \u03BB_sim")
plt.legend()
# C
plt.subplot(311)
plt.hist(C_sim, bins="rice", label="Histogramme de C_sim")
plt.legend()

plt.show()
