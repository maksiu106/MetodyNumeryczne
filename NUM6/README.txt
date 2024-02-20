W katalogu znajdują się trzy programy:

- NUM6a.py - oblicza wartości własne macierzy M z użyciem biblioteki NumPy, po czym niezależnie od tego wykonuje obliczenia z użyciem metody potęgowej - najpierw dla wyjściowej macierzy, potem ze wsparciem metody Wilkinsona o p = 3 oraz p = 4. Wypisuje na ekran wartość kryterium zbieżności w zależności od numeru iteracji, po czym podaje największą wartość własną i odpowiadający jej wektor własny.

- NUM6b.py - stosuje algorytm QR do obliczenia wartości własnych macierzy M. Wypisuje na ekran numer iteracji oraz wartość logarytmu dziesiętnego z różnic między wartościami lambda w kolejnych iteracjach.

Katalog zawiera również Makefile z komendami:
- make run - uruchamia po kolei programy NUM6a oraz NUM6b
