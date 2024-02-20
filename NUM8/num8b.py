#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import math
import random
from scipy.optimize import curve_fit

#obliczenia dla funkcji 2cos(x^3) + 0.1x^2 - 2.3
#punkty generowane w zakresie [-10, 10]

def f(x):
	return 2*math.cos(x**3) + 0.1*x**2 - 2.3
    
def perturbate():
	return random.choice([-1, 1])*random.uniform(0, perturbation)

n = int(input("Ile punktów ma zostać wygenerowane?\n"))
perturbation = float(input("Jaka ma być maksymalna wartość zaburzenia?\n"))

#macierz x-ów
A=[]
#wektor x-ów i y-ów
x=[]
y=[]

for i in range(n):
	x.append((4*i/n)-2)
	y.append(f(x[i])+perturbate())
	factors = [math.cos(x[i]**3), x[i]**2, 1]
	A.append(factors)
	
U, S, VT = np.linalg.svd(A)

print("x\ty")
for i in range(len(x)):
	print(x[i], "\t", y[i])


#konstruowanie pełnej macierzy (ST*S)^-1*ST
new_sigma = np.zeros((VT.shape[0], U.shape[1]))
for i in range(new_sigma.shape[0]):
	new_sigma[i][i] = 1/S[i]
	
result = np.dot(np.dot(np.dot(VT.T, new_sigma), U.T), y)
print("Wektor współczynników będący wynikiem wykonanej aproksymacji:")
print(result)
