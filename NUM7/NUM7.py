#!/usr/bin/env python3
#coding=utf-8

import numpy as np
import sys
import math

# 1 argument wywołania programu - stopień wielomianu, 2 - metoda wyboru punktów (a lub b) 3 - funkcja z zadania lub własna (1 lub 2)
# dla wielomianu n-tego stopnia będzie n+1 punktów doświadczalnych

def calculate_y(x, function):
	if (function == 1): return 1/(1+50*x*x)
	elif (function == 2): return math.sin(x ** 3)*math.cos(x)
	else: return 0

n = int(sys.argv[1])
mode = sys.argv[2]
function = int(sys.argv[3])

#macierz punktów
A = np.zeros((n+1, n+1))
#wektor rozwiązań
y = np.zeros(n+1)

#dla metody wyboru punktu równej a
if (mode == "a"):
	for i in range (n+1):
		point = -1 + 2*(i/(n))
		y[i] = calculate_y(point, function)
		for j in range (n+1):
			A[i,j] = point ** j
			
#dla metody wyboru punktu równej b
elif (mode == "b"):
	for i in range (n+1):
		point = math.cos(((2*i+1)*math.pi)/(2*(n+1)))
		y[i] = calculate_y(point, function)
		for j in range (n+1):
			A[i,j] = point ** j
					
result = np.linalg.solve(A, y)

print("Stopień wielomianu: ", n)
if (mode == "a"): print("Wybór węzłów jednorodny na podanym przedziale")
elif (mode == "b"): print("Wybór węzłów z wielomianu Chebysheva")
if (function == 1): print("Przybliżenie funkcji z zadania: 1/(1+50*x^2)")
elif (function == 2): print("Przybliżenie funkcji sin(x^3)*cos(x)")

print("Formuła otrzymanego wielomianu:")
polynomial = "y = "
for i in range (n+1):
	polynomial = polynomial + str(result[i]) + "*(x^" + str(i) + ") +"
polynomial = polynomial[:-1]
polynomial = polynomial.replace("+-", "-")
print(polynomial)
