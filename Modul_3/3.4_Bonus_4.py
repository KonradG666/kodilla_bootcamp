"""
Rzuty kostką
Gramy w grę polegającą na rzucaniu typową sześcienną kostką.

W każdej kolejce gracz dwukrotnie rzuca kością. Po dwukrotnym rzuceniu kością wynikiem gracza jest suma wyrzuconych oczek z rzutu numer 1 oraz rzutu numer 2.

Napisz program, który do słownika dict przypisuje pary key i value, gdzie:
    key - to możliwy do uzyskania wynik w jednej kolejce (suma oczek w dwóch rzutach)
    value - to wszystkie kombinacje rzutów, które składają się na dany key
Wszystkie możliwe kombinacje do uzyskania danego wyniku przechowuj jako zbiór, w którym każdy kolejny element to krotka, której pierwsza wartość to rezultat pierwszego rzutu, a druga wartość to rezultat drugiego rzutu.

Na przykład wywołując:
dice[7]
Wynik powinien zawierać następujące elementy:
{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}
"""
dice = {}
def dice_game(num):
    x = []
    for num in range(2, 13):
        if num not in dice.keys():
            x = list((num1, num2) for num1 in range(1,7) for num2 in range(1,7) if (num1+num2) == num)
            dice[num] = x
    print(dice)      

dice_game(7)