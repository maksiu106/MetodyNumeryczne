W katalogu znajdują się trzy programy:

- NUM4 - napisany w języku C++, przyjmuje jako argument linii poleceń wymiar macierzy A, otrzymanej po rozkładzie za pomocą wzoru Shermana-Morrisona wyjściowej macierzy

- counter - program w C++ powiązany z programem NUM4 - liczy czas wykonywania programu dla różnych N z zakresu 10 000 - 100 000, wyniki przedstawiając na standardowym wyjściu

- NUM4_alt - napisany w języku Python 3, liczy rozwiązanie równania z użyciem pakietu algebry komputerowej NumPy.

Katalog zawiera również Makefile z komendami:
- make all - do kompilacji wszystkich plików
- make clean - do usuwania plików innych niż wyjściowe
- make run - uruchamia po kolei programy NUM4, counter oraz NUM4_alt
