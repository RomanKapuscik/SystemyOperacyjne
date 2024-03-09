# SystemyOperacyjne
Skrypt na zalliczenie

W ramach zaliczenia prosty skrypt do podmiany tekstu w plikach tekstowych. Np zamiana nazwy serwera w plikach konfiguracyjnych, jeśli mamy dokonać takich zmian na 100 urządzeniach.

Można podać parametry bezpośrednio z konsoli w kolejności: ścieżka, słowo do zamiany i na jakie słowo wymieniamy.

np. py -3 plik.txt stare nowe

Skrypt:
- w pierwszej kolejnosci sprawdzi czy istnieje już katalog z backupami dla danego pliku, jesli nie to taki stworzy.
- Następnie stworzy backup pliku przed zmianą z aktualną datą i godziną.
- Sprawdzamy ile mamy backupów danego pliku, jesli więcej niż 5 to usuwamy starszse.
- Na końcu wykona podmianę w pliku docelowym


Pozdrawiam
