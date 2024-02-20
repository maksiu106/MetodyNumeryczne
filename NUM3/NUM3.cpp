#include <iostream>

int main(int argc, char *argv[])
{
	int N;
	if (argc == 1) N = 124;
	else N = atoi(argv[1]); //wymiar tablicy zadawany jest jako argument wywołania programu
	double A[4][N];

	//wypełnianie macierzy wyjściowej
 	for (int i=0; i<N; ++i)
	{
		A[0][i] = 1.2; //w macierzy A jest to diagonala (i,i); w macierzy U również
		A[1][i] = 0.2; //pod diagonalą w macierzy A; jest to (i+1,i) w macierzy L
		A[2][i] = 0.1/(double)(i+1); //nad diagonalą w macierzy A; jest to (i,i+1) w macierzy U
		A[3][i] = 0.15/((double)(i+1) * (double)(i+1)); //nad nad diagonalą w macierzy A; jest to (i,i+2) w macierzy U
	}
 	//koniec wypełniania macierzy A

 	//tworzenie wektora i wypełnienie go
 	double x[N];
 	for (int i=0; i<N; ++i) x[i] = i+1;

 	//faktoryzacja LU
 	//
 	//pierwsza kolumna wypełniana - w macierzy U jest tak samo jak w A, w macierzy L tylko jedna różnica:
 	A[1][0] = A[1][0]/A[0][0];

 	//reszta kolumn wypełniana
 	for (int i=1; i<N; ++i)
 	{
 		A[0][i] = A[0][i] - A[1][i-1]*A[2][i-1]; //diagonala macierzy U
 		A[1][i] = A[1][i]/A[0][i]; //element pod diagonalą macierzy L
 		A[2][i] = A[2][i] - A[1][i-1]*A[3][i-1]; //pierwsza skośna nad diagonalą w macierzy U
 		//A[3][i] = A[2][i]; - bez zmian, więc nawet nie ma co liczyć
 	}

 	//poniższe elementy nie istnieją - więc wypada je wyzerować
 	 A[1][N-1] = 0;
 	 A[2][N-1] = 0;
 	 A[3][N-1] = 0;
 	 A[3][N-2] = 0;

 	 double wyznacznik = 1;
 	 for (int i=0; i<N; ++i) wyznacznik = wyznacznik * A[0][i];
 	 std::cout << "Wyznacznik macierzy A, równy iloczynowi elementów na diagonali macierzy U: " << wyznacznik << std::endl;

 	 //skoro A y = x
 	 //to L (U y) = x
 	 //więc L z = x
 	 //liczenie wektora z - nadpisywanie wektora x
 	 //x[1] = 1 - nie ma co liczyć
 	 for (int i=1; i<N; ++i)
 	 {
 		 x[i] = x[i] - A[1][i-1]*x[i-1]; //niezerowe elementy macierzy L
 	 }

 	 //dwa ostatnie elementy wektora rozwiązań - liczone odrobinę inaczej niż reszta
 	 x[N-1] = x[N-1] / A[0][N-1];
 	 x[N-2] = (x[N-2] - (x[N-1] * A[2][N-2])) / A[0][N-2];
 	 //liczenie rozwiązania od końca
 	 for (int i=N-3; i>=0; --i)
 	 {
 		 x[i] = (x[i] - (x[i+1] * A[2][i]) - (x[i+2] * A[3][i])) / A[0][i];
 	 }

 	 //wypisywanie rozwiązania
 	 std::cout << "Wektor będący rozwiązaniem równania: " << std::endl;
 	 for (int i=0; i<N; ++i)
 	 {
 		 std::cout << x[i] << std::endl;
 	 }
 	 return 0;
}
