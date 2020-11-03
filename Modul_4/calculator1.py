def calculate():
    operation = int(input("""
Podaj działanie, posługując się odpowiednią liczbą:
1-Dodawanie
2-Odejmowanie
3-Mnożenie
4-Dzielenie
"""))

    while True:
        #check input
        if operation in (1,2,3,4):

            x1 = int(input("Podaj pierwszą liczbę: "))
            x2 = int(input("Podaj drugą liczkę: "))
            #addition
            if operation == 1:
                print(f"Dodaje {x1} i {x2}")
                print(f"Wynik to: ", x1 + x2)
            #subtraction
            elif operation == 2:
                print(f"Odejmuję {x2} od {x1}")
                print(f"Wynik to: ", x1 - x2)
            #multiplication
            elif operation == 3:
                print(f"Mnożę {x1} razy {x2}")
                print(f"Wynik to: ", x1 *x2)
            #division
            elif operation == 4:
                print(f"Dzielę {x1} przez {x2}")
                print(f"Wynik to: ", x1 / x2)
        #break if not in range
        else:
            print("Nie ma takiej funkcji! Zacznij jeszcze raz.")
            exit()

calculate()