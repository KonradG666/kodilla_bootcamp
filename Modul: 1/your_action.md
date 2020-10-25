Z zakresu liczb od 1 do 100 wypisz wszystkie, które są podzielne przez 3.
Spróbuj zrobić to na dwa sposoby. Użyj pętli for, jak i pętli while. Pisząc pętlę while, wykorzystaj polecenie break.
Jeśli chodzi o zadanie, podejdź do niego systemowo. Najpierw zastanów się nad tym jak zadeklarować pętlę. Jakiej kolekcji potrzebujesz?
Przed pisaniem właściwego ciała pętli zobacz czy masz poprawnie zadeklarowany początek i koniec, np. wydrukuj wszystkie elementy.

Podpowiedź #1
Jak sprawdzić czy liczba jest podzielna przez 3? Najłatwiej z użyciem wyrażenia warunkowego if oraz operatora pokazującego resztę z dzielenia (%).
Liczby podzielne przez 3 nie zostawiają reszty, więc można je w ten sposób wyselekcjonować.

division_result = i % 3

Podpowiedź #2
Jeśli chodzi o while, to stwórz pętlę, która się nie kończy, czyli taką:
while True:
pass
A następnie “wyjdź” z niej poleceniem break, gdy już liczba przekroczy 100. Liczba powinna być inkrementowana (zwiększana o 1) przy każdym przejściu pętli.

Podpowiedź #3
Pisząc pętlę for użyj już znanego Ci sposobu z funkcją range:
for i in range(101):
print(i)
