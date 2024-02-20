W katalogu znajdują się trzy programy:

- NUM3 - napisany w języku C++, przyjmuje jako argument linii poleceń wymiar macierzy A, liczy jej wyznacznik oraz dokonuje faktoryzacji LU bez wyboru elementu podstawowego, a także rozwiązuje zadanie równanie macierzowe. Wyniki wypisuje na standardowe wyjście.

- counter - program w C++ powiązany z programem NUM3 - liczy czas wykonywania programu dla różnych N z zakresu 10 000 - 100 000, a wyniki zapisuje w pliku "output.txt"

- NUM3_alt - napisany w języku Python 3, liczy rozwiązanie równania z użyciem pakietu algebry komputerowej NumPy. Liczy czas wykonywania dla różnych rozmiarów macierzy wyjściowej i wypisuje czas ich wykonywania na standardowe wyjście.

Katalog zawiera również Makefile z komendami:
- make all - do kompilacji wszystkich plików
- make clean - do usuwania plików innych niż wyjściowe
- make run - uruchamia po kolei programy NUM3, counter oraz NUM3_alt
