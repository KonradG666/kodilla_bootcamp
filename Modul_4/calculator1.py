import numpy

def calculate():
    operation = int(input("""
Wybierz funkcję, posługując się adekwatną liczbą:
1-Dodawanie
2-Odejmowanie
3-Mnożenie
4-Dzielenie
5-Exit
"""))    
    while True:
        #check input
        if operation in (1,2,3,4,5):
            
            #addition
            if operation == 1:
                print("Dodawanie")
                add_more_numbers()
            #multiplication
            elif operation == 3:
                print("Mnożenie")
                mulit_more()
            #subtraction
            if operation == 2:
                print("Odejmowanie")
                x, y =set_input()
                print(f"Odejmuję {y} od {x}")
                print(f"Wynik to: ", format(x-y, '7.2f'))
            #division
            elif operation == 4:
                print("Dzielenie")
                x, y =set_input()
                print(f"Dzielę {x} przez {y}")
                print(f"Wynik to: ", format(x / y, '7.2f'))
            elif operation == 5:
                kill_switch()
        #break if not in range
        else:
            print("Nie ma takiej funkcji! Spróbuj jeszcze raz.")
            calculate()
        #again?
        again()

#repetition
def again():
    call_it_again = input("Czy chcesz kontynuować? Y/N:")
    if call_it_again.upper() == "Y":
        calculate()
    elif call_it_again.upper() == "N":
        kill_switch()
#adding more that two numbers
def add_more_numbers():
    special_option = input("Chcesz dodać więcej cyfr jednocześnie? Y/N:")
    if special_option.upper() == "Y":
        num = list(map(int, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Dodaje: {num}")
        print(f"Wynik to: ", sum(num))
        again()
    elif special_option.upper() == "N":
        x,y = set_input()
        print(f"Dodaje {x} i {y}")
        print(f"Wynik to: ", x + y)
        again()
#multiplying more numbers

def mulit_more():
    special_option2 = input("Chcesz pomnożyć więcej cyfr jednocześnie? Y/N:")
    if special_option2.upper() == "Y":
        num = list(map(float, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Mnożę: {num} przez {num}")
        print(f"Wynik to: ", round(numpy.prod(num),2))
        again()
    elif special_option2.upper() == "N":
        x, y = set_input()
        print(f"Mnożę {x} razy {y}")
        print(f"Wynik to: ", x * y)
        again()

#set input
def set_input():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczkę: "))
    return x, y
#off
def kill_switch():
    print("Do widzenia.")
    exit()

calculate()
