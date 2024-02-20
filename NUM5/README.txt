W katalogu znajdują się trzy programy:

- Jacobi - napisany w języku C++, iteracyjnie rozwiązuje zadany układ równań za pomocą metody Jacobiego. Jako wektor startowy generowany jest losowy wektor o wartościach z przedziału [0, 10].

- Gauss - napisany w języku C++, iteracyjnie rozwiązuje zadany układ równań za pomocą metody Gaussa-Seidela. Jako wektor startowy generowany jest losowy wektor o wartościach z przedziału [0, 10].

- alternative.py - napisany w języku Python 3, liczy rozwiązanie równania z użyciem pakietu algebry komputerowej NumPy.

Katalog zawiera również Makefile z komendami:
- make all - do kompilacji wszystkich plików
- make clean - do usuwania plików innych niż wyjściowe
- make run - uruchamia po kolei programy Jacobi, Gauss oraz alternative
