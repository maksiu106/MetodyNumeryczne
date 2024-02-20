import numpy as np
import timeit

def calculate(n):
	#definiowanie macierzy A i wektora x
	A = np.eye(n)*1.2
	for i in range(n-2):
		A[i+1, i] = 0.2
		A[i, i+1] = 0.1 / (i+1)
		A[i, i+2] = 0.15 / (pow(i+1,2))
	A[n-1, n-2] = 0.2
	A[n-2, n-1] = 0.1 / (n-1)

	x = np.arange(1, n+1)

	#rozwiązanie równania macierzowego
	y = np.linalg.solve(A, x)
	return y

print("Wektor rozwiązań dla n = 124: ", calculate(124))

#mierzenie czasu
n = 1000
for i in range (10):
	start = timeit.default_timer()
	calculate(n)
	stop = timeit.default_timer()
	print("Rozmiar danych wejściowych: ", n, "; Czas wykonania: ", stop-start)
	n = n+1000
