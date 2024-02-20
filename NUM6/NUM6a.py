#!/usr/bin/env python3
#coding=utf-8

import numpy as np
from random import random

# A - macierz, y - wektor, p - parametr metody Wilkinsona
def calculate(A, y, p):
	y_last = y
	kryterium = 100 #kryterium zbieżności - norma z różnicy wektorów w kolejnych iteracjach
	n=0 #licznik wykonanych iteracji
	
	print("iteracja\tlog(10)(wektor niezaburzony)\tlog(10)")
	while (kryterium > 1e-12 and n < 1000):
		y = np.dot(A, y)
		norm = np.linalg.norm(y)
		for i in range(4): y[i] = y[i]/norm
		kryterium = np.linalg.norm(y - y_last)
		print(n+1, "\t", np.log10(kryterium))
		n = n + 1
		y_last = y
	
	print("Wektor własny o największej wartości własnej: ", y)
	print("Wartość własna dla niego, a więc największa wartość własna danej macierzy:", np.dot(A, y)[0]/y[0]+p)

#macierz wyjściowa
A = np.array([[8, 1, 0, 0], [1, 7, 2, 0], [0, 2, 6, 3], [0, 0, 3, 5]])

#tworzenie losowego wektora o wartościach z przedziału [0, 10]
y = np.random.rand(4)
for i in range(4): y[i] *= 10

print("Wartości własne obliczone z użyciem biblioteki NumPy: ", np.linalg.eigvals(A))
print("Losowo wygenerowany do obliczeń wektor y: ", y)
print("\nOBLICZENIA DLA MACIERZY, NA KTÓREJ NIE UŻYWA SIĘ METODY WILKINSONA")
calculate(A, y, 0)

print("\nOBLICZENIA DLA MACIERZY, NA KTÓREJ UŻYTO METODĘ WILKINSONA DLA P = 3")
np.fill_diagonal(A, A.diagonal() - 3)
calculate(A, y, 3)

print("\nOBLICZENIA DLA MACIERZY, NA KTÓREJ UŻYTO METODĘ WILKINSONA DLA P = 4")
np.fill_diagonal(A, A.diagonal() - 1)
calculate(A, y, 4)

