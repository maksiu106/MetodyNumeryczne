#!/usr/bin/env python3
#coding=utf-8

import numpy as np

A1 = [[2.554219275, 0.871733993, 0.052575899, 0.240740262, 0.316022841],
	[0.871733993, 0.553460938, -0.070921727, 0.255463951, 0.707334556],
	[0.052575899, -0.070921727, 3.409888776, 0.293510439, 0.847758171],
	[0.240740262, 0.255463951, 0.293510439, 1.108336850, -0.206925123],
	[0.316022841, 0.707334556, 0.847758171, -0.206925123, 2.374094162]]
	
A2 = [[2.645152285, 0.544589368, 0.009976745, 0.327869824, 0.424193304],
	[0.544589368, 1.730410927, 0.082334875, -0.057997220, 0.318175706],
	[0.009976745, 0.082334875, 3.429845092, 0.252693077, 0.797083832],
	[0.327869824, -0.057997220, 0.252693077, 1.191822050, -0.103279098],
	[0.424193304, 0.318175706, 0.797083832, -0.103279098, 2.502769647]]
	
b = [[-0.642912346], [-1.408195475], [4.595622394], [-5.073473196], [2.178020609]]
	
b = np.array(b)

y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)

print("Niezaburzony wektor rozwiązań y1:\n", y1)
print("Niezaburzony wektor rozwiązań y2:\n", y2)

perturbation = np.random.rand(5) #generowanie losowego wektora zaburzeń
perturbation = (perturbation * 10e-6 / np.linalg.norm(perturbation)) #skalowanie wektora, żeby jego norma wynosiła 10^-6

b = np.add(b,perturbation.reshape(-1,1)) #dodawanie wektora zaburzeń do wyjściowego wektora

print("\nWektor b po zaburzeniu:\n", b)

y1 = np.linalg.solve(A1, b)
y2 = np.linalg.solve(A2, b)

print("\nZaburzony wektor rozwiązań y1':\n", y1)
print("Zaburzony wektor rozwiązań y2':\n", y2)
