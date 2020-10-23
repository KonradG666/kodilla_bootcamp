"""Stwórz słownik imion
Do zmiennej names została przypisana lista imion męskich.

Stwórz słownik, którego kluczami będą pierwsze litery imion w liście names, a wartościami będą wszystkie imiona, które zaczynają się na daną literę.
Słownik przypisz do zmiennej name_dict.

Na przykład:
name_dict['P'] powinien zwracać imiona: Paweł, Piotr

Podpowiedź
Miej na uwadze, że imiona w słowniku nie powinny się powtarzać!"""

names = ['Paweł', 'Kewin', 'Ireneusz', 'Bolesław', 'Mateusz', 'Edward', 'Piotr', 'Jan', 'Denis', 'Amir',
         'Igor', 'Borys', 'Robert', 'Ariel', 'Kuba', 'Rafał', 'Mateusz', 'Emanuel', 'Alfred', 'Artur', 'Jakub',
         'Ludwik', 'Bolesław', 'Remigiusz', 'Martin', 'Dobromił', 'Mariusz', 'Amadeusz', 'Łukasz', 'Bolesław', 'Amir',
         'Artur', 'Albert', 'Olgierd', 'Alek', 'Kordian', 'Julian', 'Anastazy', 'Emanuel', 'Józef']

name_dict = {}
# to remove duplicated
names = set(names)
# create list with names first letter
first_letter = [x[0] for x in names]

# check if the letter is in the list

for name in names:
    first_letter = name[0]
    # if letter in append the name
    if first_letter in name_dict:
        name_dict[first_letter].append(name)
    # if letter not in create new and append
    else:
        name_dict[first_letter] = [name]

print(f"ditc: {name_dict}")
print(" ")
# print(f"letters: {first_letter}")


count = 0
for key, value in name_dict.items():
    if isinstance(value, list):
        count += len(value)
print("The number of elements in lists: \n", count)
