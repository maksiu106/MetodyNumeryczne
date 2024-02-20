#include <iostream>

int main(int argc, char *argv[])
{
	int N;
	if (argc == 1) N = 80;
	else N = atoi(argv[1]); //wymiar tablicy zadawany jest jako argument wywołania programu

	double y[N], z[N];
	y[N] = 5/11;
	z[N] = 1/11;

	//Ay = b
	//Az = u
	//A to macierz z 11 na diagonali i 7 nad nią
	//b to wektor wyrazów wolnych - same 5
	//u to wektor samych jedynek
	for (int i=N-1; i>=0; --i)
	{
		y[i] = (5 - 7*y[i+1])/11;
		z[i] = (1 - 7*z[i+1])/11;
	}

	//mianownik z wyrażenia na x oraz czynnik v^T * y
	double mianownik = 1;
	double vTy = 0;
	for (int i=0; i<N; ++i)
	{
		mianownik += z[i];
		vTy += y[i];
	}

	//liczenie wektora rozwiązań i wypisywanie go
	std::cout << "Wektor rozwiązań dla N = " << N << std::endl;
	for (int i=0; i<N; ++i)
	{
		z[i] = (z[i] * vTy)/mianownik; //wyrażenie odejmowane od wektora y we wzorze
		y[i] -= z[i];
		std::cout << y[i] << std::endl;
	}
}
