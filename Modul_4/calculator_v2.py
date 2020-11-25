import numpy

op_dodawanie = 1
op_dejmowanie = 2
op_mnożenie = 3
op_dzielenie = 4
op_exit = 5
op_decimal_point = 6

operation_list = ["Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie", "Exit"]

decimal_point = "7.2f"

allowed_operactions = [
    op_dodawanie , op_dejmowanie , op_mnożenie , op_dzielenie , op_exit, op_decimal_point 
]
def calculate():
    display(operation_list)
    operation = int(input("Please selcet acction: "))
    print(operation)
    while True:
        #check input
        if operation not in allowed_operactions:
            print("Nie ma takiej funkcji! Spróbuj jeszcze raz.")
            calculate()           
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
            print(f"Wynik to: ", format(x-y, decimal_point))
        #division
        elif operation == 4:
            print("Dzielenie")
            x, y =set_input()
            print(f"Dzielę {x} przez {y}")
            print(f"Wynik to: ", format(x / y, decimal_point))
        elif operation == 5:
            kill_switch()
        elif operation == 6:
            set_decimals()
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
        num = list(map(float, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Dodaje: {num}")
        score_for_num = sum(num)
        print(f"Wynik to: ", format(numpy.prod(score_for_num), decimal_point))
        
    elif special_option.upper() == "N":
        x,y = set_input()
        print(f"Dodaje {x} i {y}")
        print(f"Wynik to: ", format((x + y), decimal_point))
        
#multiplying more numbers

def mulit_more():
    special_option2 = input("Chcesz pomnożyć więcej cyfr jednocześnie? Y/N:")
    if special_option2.upper() == "Y":
        num = list(map(float, input("Podaj liczby (oddzielone spacją): ").split()))
        print(f"Mnożę: {num} przez {num}")
        print(f"Wynik to: ", format(numpy.prod(num), decimal_point))
        
    elif special_option2.upper() == "N":
        x, y = set_input()
        print(f"Mnożę {x} razy {y}")
        print(f"Wynik to: ", format(( x * y), decimal_point))
        
#set input
def set_input():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczkę: "))
    return x, y
#how many zeros
def set_decimals():
    global decimal_point
    ndp = input("How many zeros after comma?: ")
    print(ndp)
    decimal_point = "7.{}f".format(ndp)
    print(f"New Decimal point", decimal_point)
#display
def display(operation_list):
    counter = 0
    record = {}
    for tables in operation_list:
        counter += 1
        record[counter] = tables
        print("%s. %s" % (counter, tables))
    return record

#off
def kill_switch():
    print("Do widzenia.")
    exit()

calculate()
