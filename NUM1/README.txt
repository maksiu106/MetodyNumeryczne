W katalogu zawarto sprawozdanie w formacie pdf, kod programu w formacie cpp oraz plik Makefile.

W pliku Makefile zdefiniowano komendy:
- Make all - służy do kompilacji programu
- Make run - uruchamia program
- Make tar - kompresuje program do formatu .tar.gz
- Make clean - usuwa wszystkie skompilowane pliki oraz plik wynikowy output.txt

W formie przeslanej do oceny program jest ustawiony do wykonywania obliczen dla typu float oraz pierwszego z dwoch wzorow podanych w skrypcie. Aby wykonac obliczenia dla drugiego wzoru, na gorze kodu w dyrektywach preprocesora nalezy zmienic definicje slowa kluczowego WZOR na wzor_b. Aby wykonac obliczenia na typie double, w podobny sposob nalezy zmienic definicje slowa TYP na double; ponadto dobrze jest wowczas zmienic w linii 47. krok, z jakim zmienia sie wartosc h, aby obliczenia nie trwaly godzinami - w swoich obliczeniach przemnozylem go o wartosc 100 000.
