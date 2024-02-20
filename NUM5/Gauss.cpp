#include <iostream>
#include <random>
#include <math.h>
#include <iomanip>

#define N 124

int main()
{
	double b[N]; //wektor wyrazów wolnych
	double x[N]; //wektor na iterowane rozwiązanie
	double last[N];

	double norma = 1000; //norma różnicy między kolejnymi iteracjami
	int n = 0; //ilość wykonanych iteracji

	srand(time(NULL));
	for (int i=0; i<N; ++i)
	{
		for (int i=0; i<N; ++i) b[i] = i+1; //wyrazy wolne
		last[i] = 10.0*(double)rand()/(double)RAND_MAX; //losowo wybrany punkt startowy
	}

	std::cout << "Iteracja:\tLog(10) z normy:" << std::endl;
	//Jacobi
	while (norma > 1e-12)
	{
		++n;
		//skrajne przypadki na końcu wektora, gdzie inne elementy będą się zerować
		x[0] = (b[0] - last[1] - 0.15*last[2])/3;
		x[1] = (b[1] - x[0] - last[2] - 0.15*last[3])/3;
		x[N-2] = (b[N-2] - last[N-1] - x[N-3] - 0.15*x[N-4])/3;
		x[N-1] = (b[N-1] - x[N-2] - 0.15*x[N-3])/3;
		//metoda dla całego wektora
		for (int i=2; i<N-2; ++i)
		{
			x[i] = (b[i] - x[i-1] - last[i+1] - 0.15*x[i-2] - 0.15*last[i+2])/3;
		}

		//liczenie normy z różnicy między wektorami
		double suma = 0;
		for (int i=0; i<N; ++i)
		{
			suma += pow((x[i]-last[i]),2);
		}
		norma = sqrt(suma);

		std::cout << n << "\t" << log10(norma) << std::endl;

		//przepisanie wektora x do wektora last
		for (int i=0; i<N; ++i) last[i] = x[i];
	}

	std::cout << std::endl << "Wektor rozwiązań uzyskany po " << n << " iteracjach przy normie różnicy kolejnych wektorow wynoszacej: " << norma << std::endl;
	for (int i=0; i<N; ++i)
	{
		std::cout << std::setprecision(14) << x[i] << std::endl;
	}
}
