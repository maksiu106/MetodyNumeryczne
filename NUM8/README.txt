W katalogu znajdują się dwa programy:
- num8a.py - przyjmuje on jeden argument wejściowy - ścieżkę do pliku, w którym zebrane są punkty pomiarowe pobrane z platformy Pegaz (tutaj: in.txt)
- num8b.py - generuje od punkty pomiarowe oraz wykonuje aproksymację dla funkcji 2cos(x^3) + 0.1x^2 - 2.3, generując podaną z klawiatury ilość punktów posiadających losowe zaburzenia w zakresie również podanym z klawiatury

Katalog zawiera również Makefile z komendami:
- make run - uruchamia program num8a z domyślnym plikiem zawierającym dane (in.txt) oraz program num8b
