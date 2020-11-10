import numpy

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
            
            #addition
            if operation == 1:
                print("Dodawanie")
                add_more_numbers()
            #multiplication
            elif operation == 3:
                print("Mnożenie")
                mulit_more()

            #x1 = int(input("Podaj pierwszą liczbę: "))
            #x2 = int(input("Podaj drugą liczkę: "))
            #subtraction
            if operation == 2:
                print("Odejmowanie")
                set_input()
                print(f"Odejmuję {x2} od {x1}")
                print(f"Wynik to: ", x1 - x2)
            #division
            elif operation == 4:
                print("Dzielenie")
                set_input()
                print(f"Dzielę {x1} przez {x2}")
                print(f"Wynik to: ", x1 / x2)
        #break if not in range
        else:
            print("Nie ma takiej funkcji! Zacznij jeszcze raz.")
            calculate()
        #again?
        again()

#repetition
def again():
    call_it_again = input("Czy chcesz kontynuować? Y/N:")
    if call_it_again.upper() == "Y":
        calculate()
    elif call_it_again.upper() == "N":
        print("Do widzenia.")
        exit()
#adding more that two numbers
def add_more_numbers():
    special_option = input("Chcesz dodać więcej cyfr jednocześnie? Y/N:")
    if special_option.upper() == "Y":
        num = list(map(int, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Dodaje: {num}")
        print(f"Wynik to: ", sum(num))
        again()
    elif special_option.upper() == "N":
        set_input()
        print(f"Dodaje {x} i {y}")
        print(f"Wynik to: ", x + y)
        again()
#multiplying more numbers

def mulit_more():
    special_option2 = input("Chcesz pomnożyć więcej cyfr jednocześnie? Y/N:")
    if special_option2.upper() == "Y":
        num = list(map(int, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Mnożę: {num} przez {num}")
        print(f"Wynik to: ", numpy.prod(num))
        again()
    elif special_option2.upper() == "N":
        set_input()
        print(f"Mnożę {x} razy {y}")
        print(f"Wynik to: ", x * y)
        again()

#set input
def set_input():
    x = int(input("Podaj pierwszą liczbę: "))
    y = int(input("Podaj drugą liczkę: "))
    return x, y

calculate()
