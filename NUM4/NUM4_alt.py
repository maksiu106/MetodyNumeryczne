import numpy as np
import timeit

def calculate(n):
	#definiowanie macierzy A i wektora x
	A = np.eye(n)*11
	for i in range(n):
		for j in range(n):
			A[i][j] += 1
	for i in range(n-1):
		A[i][i+1] += 7
	x = np.full(n, 5)

	#rozwiązanie równania macierzowego
	y = np.linalg.solve(A, x)
	return y

print("Wektor rozwiązań dla n = 80: ", calculate(80))
