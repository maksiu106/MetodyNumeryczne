#!/usr/bin/env python3
#coding=utf-8

import numpy as np

#macierz wyjściowa
A = np.array([[8, 1, 0, 0], [1, 7, 2, 0], [0, 2, 6, 3], [0, 0, 3, 5]])

lambda1 = A[0,0]
lambda2 = A[1,1]
lambda3 = A[2,2]
lambda4 = A[3,3]
last_l1 = 0
last_l2 = 0
last_l3 = 0
last_l4 = 0
n=0 #licznik wykonanych iteracji

print("Iteracja\tlog10(l1)\tlog10(l2)\tlog10(l3)\tlog10(l4)")

while ((abs(lambda1-last_l1) > 1e-12 or abs(lambda2-last_l2) > 1e-12 or abs(lambda3-last_l3) > 1e-12 or abs(lambda4-last_l4) > 1e-12) and n < 1000):
	Q, R = np.linalg.qr(A)
	A = np.dot(R, Q)
	last_l1 = lambda1
	last_l2 = lambda2
	last_l3 = lambda3
	last_l4 = lambda4
	lambda1 = A[0,0]
	lambda2 = A[1,1]
	lambda3 = A[2,2]
	lambda4 = A[3,3]
	print(n+1, "\t", np.log10(abs(lambda1-last_l1)), "\t", np.log10(abs(lambda2-last_l2)), "\t", np.log10(abs(lambda3-last_l3)), "\t", np.log10(abs(lambda4-last_l4)))
	n+=1
	
print("Ukończono obliczenia")
print("Wartości własne macierzy A: ", lambda1, "\t", lambda2, "\t", lambda3, "\t", lambda4)
print("Macierz A po przekształceniach: ")
print(A)

	
