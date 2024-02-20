#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import sys
import math
from scipy.optimize import curve_fit

#dane wejściowe są w pliku o nazwie, która ma być argumentem wywołania programu

data = np.loadtxt(sys.argv[1], delimiter=',')
#macierz x-ów
A=[]
#wektor y-ów
y=[]

for row in data:
	factors = [row[0]**2, math.sin(row[0]), math.cos(5*row[0]), math.exp(-row[0])]
	A.append(factors)
	y.append(row[1])
	
U, S, VT = np.linalg.svd(A)

#konstruowanie pełnej macierzy (ST*S)^-1*ST
new_sigma = np.zeros((VT.shape[0], U.shape[1]))
for i in range(new_sigma.shape[0]):
	new_sigma[i][i] = 1/S[i]
	
result = np.dot(np.dot(np.dot(VT.T, new_sigma), U.T), y)
print("Wektor współczynników będący wynikiem wykonanej aproksymacji:")
print(result)

#sprawdzenie wyniku z użyciem biblioteki

def func(x, a, b, c, d):
	return a * x**2 + b * np.sin(x) + c * np.cos(5*x) + d * np.exp(-x)

parameters = (curve_fit(func, data[:, 0], y))[0]
print("Wektor współczynników obliczonych z użyciem biblioteki:")
print(parameters)
