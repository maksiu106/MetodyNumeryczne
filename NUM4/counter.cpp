#include <iostream>
#include <chrono>

//przepisana funkcja NUM4 z usunięciem wszystkich std::cout
void run(int N)
{
	double y[N], z[N];
	y[N] = 5/11;
	z[N] = 1/11;

	for (int i=N-1; i>=0; --i)
	{
		y[i] = (5 - 7*y[i+1])/11;
		z[i] = (1 - 7*z[i+1])/11;
	}

	double mianownik = 1;
	double vTy = 0;
	for (int i=0; i<N; ++i)
	{
		mianownik += z[i];
		vTy += y[i];
	}

	for (int i=0; i<N; ++i)
	{
		z[i] = (z[i] * vTy)/mianownik;
		y[i] -= z[i];
	}
}

int main()
{
	std::cout << "Uruchomiono program, który rozwiąże równanie macierzowe z zadania NUM4 dla zmiennych danych wejściowych w zakresie 10 000 - 100 000 z krokiem 10 000, dla każdej z wartości wykonując 5000 powtórzeń, żeby dokładniej zmierzyć czas wykonania" << std::endl;
	int n = 10000; //rozmiar danych wejściowych
	int times = 5000; //ilość powtó©zeń
	for (int i=0; i<10; ++i)
	{
		auto start = std::chrono::high_resolution_clock::now();
		for (int j=0; j<times; ++j) run(n);
		auto stop = std::chrono::high_resolution_clock::now();
		std::chrono::duration<double> result = (stop - start);
		std::cout << "Wymiar macierzy: " << n << "\t" << "Czas: " << result.count()/(double)times << std::endl;
		n+=10000;
	}
}
