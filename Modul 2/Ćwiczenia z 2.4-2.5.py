print("Moduł 2.4")
print("__1__")
vegetables = ["burak", "ziemniak", "szczypior", "cebula"]
for vegetable in vegetables:
    print(vegetable)
print("")
veggie_iterator = iter(vegetables)
print(veggie_iterator)
for vegetable in veggie_iterator:
    print(vegetable)
print("__2__")
veggie_iterator = iter(vegetables)
print(next(veggie_iterator))
print(next(veggie_iterator))
print(next(veggie_iterator))
print(next(veggie_iterator))
# print(next(veggie_iterator)) |za mało argumentøw w liscie = Traceback (most recent call last): File '"main.py", line 15 in <module> oprint(next(vegetable_iteration)) StopIteration.
print("_____________________________________________________________________")
print("")
shopping = [("buraki", 1.25), ("mleko", 4.0), ("chleb", 3.50), ("wino", 15)]
for product, price in shopping:
    print(product)
print("")
shopping_dict = dict(shopping)
print(shopping_dict)
print("")
for product in shopping_dict:
    print(product)
print("")
for product in shopping_dict.items():
    print(product)
print("_____________________________________________________________________")
print("__3__")
neighbour_countres = [("Niemcy", "Berlin"), ("Czech", "Praga"), ("Słowacja", "Bratysława"), ("Ukraina", "Kijow"),
                      ("Białorus", "Minsk"), ("Litwa", "Wilno"), ("Rosja", "Moskwa")]
print(neighbour_countres)
print("")
neighbour_countres = dict(neighbour_countres)
print(neighbour_countres)
print("")
for countrie in neighbour_countres:
    print(countrie)
print("")
for countrie in neighbour_countres.items():
    print(countrie)
print("_____________________________________________________________________")
print("Moduł 2.5")
numbers = [1, 3, 5, 11, 20]
squares = []
for number in numbers:
    squares.append(number * number)
print(f"Na wstępie mieliśmy taką listę {numbers}")
print(f"A oto jej kwadraty {squares}")
print("")
squares = [number * number for number in numbers]
print(f"Te kwadraty {squares} uzyskano dzięki list comprehension")
print("__1__")
percentage = [number + (0.22 * number) for number in numbers]
print(f"Dodano 22% do każdej liczby z listy otrzymując wynik: {percentage} uzyskano dzięki list comprehension")
print("")
numbers = [1, 2, 0, 3, 0, 0, 0]
squares = []
for number in numbers:
    if number > 0:
        squares.append(number * number)
print(numbers)
print(f"Squares of numbers are: {squares}")
print("")
numbers = [1, 2, 0, 3, 0, 0, 0]
squares = [number * number for number in numbers if number > 0]
print(f"Squares of numbers are: {squares} With usage of list comprehension.")
print("_____________________________________________________________________")
print("__2__")
print("")
name_list = ["Arystoteles", "Platon", "Sokrates"]
print(name_list)
new_name_list_1 = []
for word in name_list:
    new_name_list_1.append(len(word))
print(new_name_list_1)
print("")
letter_count = [len(word) for word in name_list]
print(f"{letter_count} printed with list comprehension.")
print("_____________________________________________________________________")
print("Slicing")
weekdays = ["pon", "wto", "śro", "czw", "pią", "sob", "nie"]
# indeks:     0      1      2      3      4      5      6
print("whole week: {}".format(weekdays))
print("First two days: {}".format(weekdays[0:2]))
print("Mid-week: {}".format(weekdays[3:6]))
print("First four days: {}".format(weekdays[:4]))
