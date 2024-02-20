import numpy as np
import timeit

def calculate(n):
	#definiowanie macierzy A i wektora x
	A = np.eye(n)*3
	for i in range(n-2):
		A[i+2, i] = 0.15
		A[i+1, i] = 1
		A[i, i+1] = 1
		A[i, i+2] = 0.15
	A[n-1, n-2] = 1
	A[n-2, n-1] = 1
	
	print(A)

	x = np.arange(1, n+1)

	#rozwiązanie równania macierzowego
	y = np.linalg.solve(A, x)
	return y

np.set_printoptions(precision=14)
print("Wektor rozwiązań dla n = 124: ", calculate(124))
