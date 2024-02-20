#include <iostream>
#include <fstream>
#include <cmath>

//przy obliczeniach dla typu double wystarczy zmienic TYP w dyrektywie preprocesora
#define TYP float
#define WZOR wzor_a

//ta funkcja liczy blad wedlug wzoru (a) ze skryptu
TYP wzor_a (char funkcja, TYP x, TYP h)
{
	TYP blad;
	//dla sinusa
	if (funkcja=='a') blad = ((TYP)sin((TYP)(x+h)*(x+h))-(TYP)sin((TYP)x*x))/h - (TYP)2*x*cos((TYP)x*x);
	//dla cosinusa
	else if (funkcja=='b') blad = ((TYP)cos((TYP)(x+h)*(x+h))-(TYP)cos((TYP)x*x))/h + (TYP)2*x*sin((TYP)x*x);
	if (blad<0) blad = -blad;
	return blad;
}

//ta funkcja liczy blad wedlug wzoru (b) ze skryptu
TYP wzor_b (char funkcja, TYP x, TYP h)
{
	TYP blad;
	//dla sinusa
	if (funkcja=='a') blad = ((TYP)sin((TYP)(x+h)*(x+h))-(TYP)sin((TYP)(x-h)*(x-h)))/(2*h) - (TYP)2*x*cos((TYP)x*x);
	//dla cosinusa
	else if (funkcja=='b') blad = ((TYP)cos((TYP)(x+h)*(x+h))-(TYP)cos((TYP)(x-h)*(x-h)))/(2*h) + (TYP)2*x*sin((TYP)x*x);
	if (blad<0) blad = -blad;
	return blad;
}

int main()
{
	//zbieranie danych wejsciowych
	std::cout << "Ten program policzy blad numerycznego przyblizenia pochodnej dla zmiennej typu zdefiniowanego w poleceniach preprocesora w zaleznosci od zmiany parametru h" << std::endl;
	std::cout << "Dla jakiej funkcji chcesz wykonac obliczenia?\n (a) sin(x^2)\n (b) cos(x^2)" << std::endl;
	char funkcja;
	TYP punkt;
	std::cin >> funkcja;
	std::cout << "W jakim punkcie funkcja ma byc badana?" << std::endl;
	std::cin >> punkt;

	std::ofstream zapisuj("output.txt");
	TYP krok = std::numeric_limits<TYP>::epsilon();

	for (TYP h = krok; h<0.1; h=h+krok)
	{
		std::cout << h << std::endl;
		zapisuj << (TYP)log10(h) << "\t" << (TYP)log10((TYP)WZOR(funkcja, punkt, h)) << std::endl;
	}
}
