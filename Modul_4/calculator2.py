
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
            #multiple values intake
            num = list(map(int, input("Podaj liczby (oddzielone spacją): ").split()))
            print(f"numlist: {num}")
            #addition
            if operation == 1:
                print(f"Dodaje: {num}")
                print(f"Wynik to: ", sum(num))
            #subtraction
            elif operation == 2:
                print(f"Odejmuję {num}")
                print(f"Wynik to: ", (num[0]-sum(num[1:])))
            #multiplication
            elif operation == 3:
                print(f"Mnożę {num} przez {num}")
                print(f"Wynik to: ", multiply(num))
            #division
            elif operation == 4:
                print(f"Dzielę {x1} przez {x2}")
                print(f"Wynik to: ", x1 / x2)
        #break if not in range
        else:
            print("Nie ma takiej funkcji! Zacznij jeszcze raz.")
            calculate()

calculate()