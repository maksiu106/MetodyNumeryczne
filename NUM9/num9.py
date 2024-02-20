#!/usr/bin/env python3
#coding=utf-8

import math

epsilon = 1e-12
result = math.asin(0.4)

def f(x):
	return math.sin(x)-0.4
	
def f_der(x):
	return math.cos(x)
	
def g(x):
	return math.pow(f(x), 2)
	
def g_der(x):
	return 2*math.cos(x)*f(x)
	
#do liczenia h(x) = g(x)/g'(x)
def h(x):
	return f(x)/(2*math.cos(x))
	
def h_der(x):
	return (0.8*math.sin(x) + 2)/(4*math.pow(math.cos(x),2))
	
def bisekcja(fun):
	a = 0
	b = math.pi/4
	i = 0
	if (fun(a)*fun(b) > 0):
		print("Musisz użyć innych punktów startowych dla tej funkcji")
		return
	print("Zastosowanie metody bisekcji")
	print("Iteracja\tRóżnica między x_i a wartością dokładną")
	last = 10
	c = 20
	while (abs(c-last) > epsilon):
		print(i, "\t", abs(result - c))
		i = i+1
		last = c
		c = (a+b)/2
		if (fun(a)*fun(c) < 0): b = c
		elif (fun(c)*fun(b) < 0): a = c
		if (i > 100):
			print("Przerwano metodę ze względu na brak zbieżności")
			break
	print(i, "\t", abs(result - c))
	print("Otrzymano miejsce zerowe w punkcie ", c, "\n")
	
def falsi(fun):
	a = 0
	b = math.pi/4
	i = 0
	if (fun(a)*fun(b) > 0):
		print("Musisz użyć innych punktów startowych dla tej funkcji")
		return
	print("Zastosowanie metody falsi")
	print("Iteracja\tRóżnica między x_i a wartością dokładną")
	last = 10
	c = 20
	while (abs(c-result) > epsilon):
		print(i, "\t", abs(c-result))
		i = i+1
		last = c
		c = (a*fun(b) - b*fun(a))/(fun(b) - fun(a))
		if (fun(a)*fun(c) < 0): b = c
		elif (fun(c)*fun(b) < 0): a = c
		if (i > 100):
			print("Przerwano metodę ze względu na brak zbieżności")
			break
	print(i, "\t", abs(c-result))
	print("Otrzymano miejsce zerowe w punkcie ", c, "\n")

def sieczne(fun):
	last = 1
	x = math.pi/4
	i = 0
	print("Zastosowanie metody siecznych")
	print("Iteracja\tRóżnica między x_i a wartością dokładną")
	while (abs(last-x) > epsilon):
		print(i, "\t", abs(x-result))
		i = i+1
		temp = x
		x = (x*fun(last) - last*fun(x))/(fun(last)-fun(x))
		last = temp
		if (i > 100):
			print("Przerwano metodę ze względu na brak zbieżności")
			return
	print(i, "\t", abs(x-result))
	print("Otrzymano miejsce zerowe w punkcie ", x, "\n")
	
def newton(fun, fun_der):
	last = 10
	x = math.pi/4
	i = 0
	print("Zastosowanie metody Newtona")
	print("Iteracja\tRóżnica między x_i a wartością dokładną")
	while (abs(last-x) > epsilon):
		print(i, "\t", abs(result-x))
		i = i+1
		last = x
		x = x - (fun(x)/fun_der(x))
		if (i > 100):
			print("Przerwano metodę ze względu na brak zbieżności")
			return
	print(i, "\t", abs(result-x))
	print("Otrzymano miejsce zerowe w punkcie ", x, "\n")

def main():
	print("BADANIE FUNKCJI F(X) = SIN(X) - 0.4\n")
	bisekcja(f)
	falsi(f)
	sieczne(f)
	newton(f, f_der)
	
	print("BADANIE FUNKCJI G(X) = F(X)^2\n")
	sieczne(g)
	newton(g, g_der)
	
	print("BADANIE FUNKCJI G(X) = F(X)^2 SPRYTNIEJSZĄ METODĄ\n")
	bisekcja(h)
	falsi(h)
	sieczne(h)
	newton(h, h_der)
	
if __name__ == "__main__":
	main()
	
