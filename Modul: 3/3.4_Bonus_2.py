"""
Stwórz funkcję, która sprawdza, czy możemy zbudować most
Naszym zadaniem jest zbudowanie mostu pomiędzy punktem A i punktem B.

Do dyspozycji mamy dwa rodzaje płyt, które mają określoną długość.
Płyt nie możemy dzielić na mniejsze części, możemy je układać tylko jedna obok drugiej.

Stwórz funkcję build_bridge, która jako argumenty będzie zwracać wartość True, jeśli mając mniejszą płytę o długości danej zmienną small oraz 
większą płytę o długości danej zmienną big jesteśmy w stanie zbudować most od długości danej zmienną goal.

Niech funkcja build_bridge zwraca wartość False, jeśli zbudowanie mostu przy założeniu zmiennych small, big oraz goal nie jest możliwe.


Na przykład:
Jeśli goal to 37, small to 2, a big to 5. Wtedy możemy zbudować most, a funkcja powinna
zwracać wartość True.

7 * big + 1 * small = goal
7 * 5 + 1 * 2 = 37






Z drugiej strony, jeśli goal to 37, small to 3, a big to 5. Wtedy NIE możemy zbudować
mostu, a funkcja powinna zwracać wartość False.
"""
def build_bridge(small, big, goal):
  # goal - odległość do wypełnienia
  # small - długość mniejszej płyty
  # big - długość większej płyty
    return pass # Zwróć wartość True jeśli można zbudować most
                #lub False jeśli nie możemy go zbudować
