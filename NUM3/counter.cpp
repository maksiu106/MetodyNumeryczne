#include <iostream>
#include <chrono>
#include <fstream>

//przepisana funkcja NUM3 z usunięciem wszystkich std::cout
void run(int N)
{
	double A[4][N];

 	for (int i=0; i<N; ++i)
	{
		A[0][i] = 1.2; //w macierzy A jest to diagonala (i,i); w macierzy U również
		A[1][i] = 0.2; //pod diagonalą w macierzy A; jest to (i+1,i) w macierzy L
		A[2][i] = 0.1/(double)(i+1); //nad diagonalą w macierzy A; jest to (i,i+1) w macierzy U
		A[3][i] = 0.15/((double)(i+1) * (double)(i+1)); //nad nad diagonalą w macierzy A; jest to (i,i+2) w macierzy U
	}
 	double x[N];
 	for (int i=0; i<N; ++i) x[i] = i+1;
 	A[1][0] = A[1][0]/A[0][0];
 	for (int i=1; i<N; ++i)
 	{
 		A[0][i] = A[0][i] - A[1][i-1]*A[2][i-1]; //diagonala macierzy U
 		A[1][i] = A[1][i]/A[0][i]; //element pod diagonalą macierzy L
 		A[2][i] = A[2][i] - A[1][i-1]*A[3][i-1]; //pierwsza skośna nad diagonalą w macierzy U
 	}
 	 A[1][N-1] = 0;
 	 A[2][N-1] = 0;
 	 A[3][N-1] = 0;
 	 A[3][N-2] = 0;
 	 for (int i=1; i<N; ++i)
 	 {
 		 x[i] = x[i] - A[1][i-1]*x[i-1]; //niezerowe elementy macierzy L
 	 }

 	 x[N-1] = x[N-1] / A[0][N-1];
 	 x[N-2] = (x[N-2] - (x[N-1] * A[2][N-2])) / A[0][N-2];
 	 for (int i=N-3; i>=0; --i)
 	 {
 		 x[i] = (x[i] - (x[i+1] * A[2][i]) - (x[i+2] * A[3][i])) / A[0][i];
 	 }
}

int main()
{
	std::ofstream plik;
	plik.open("output.txt");
	std::cout << "Uruchomiono program, który rozwiąże równanie macierzowe z zadania NUM3 dla zmiennych danych wejściowych w zakresie 10 000 - 100 000 z krokiem 10 000, dla każdej z wartości wykonując 5000 powtórzeń, żeby dokładniej zmierzyć czas wykonania" << std::endl;
	int n = 10000; //rozmiar danych wejściowych
	int times = 5000; //ilość powtó©zeń
	for (int i=0; i<10; ++i)
	{
		auto start = std::chrono::high_resolution_clock::now();
		for (int j=0; j<times; ++j) run(n);
		auto stop = std::chrono::high_resolution_clock::now();
		std::chrono::duration<double> result = (stop - start);
		plik << n << "\t" << result.count()/(double)times << std::endl;
		std::cout << "Zakończono " << i+1 << " iterację na 10 do wykonania" << std::endl;
		n+=10000;
	}
	plik.close();
}
