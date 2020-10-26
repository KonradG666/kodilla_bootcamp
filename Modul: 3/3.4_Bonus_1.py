"""
Znajdź średnią zmodyfikowanej listy
Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej numbers w taki sposób, aby każdy jej element zaokrąglić do pełnej dziesiątki. 
Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą numbers, lecz zmodyfikować listę numbers.

Po zaokrągleniu każdego elementu listy numbers, pozbądź się jej największego oraz najmniejszego elementu, 
a następnie do zmiennej mean_number przypisz średnią z ostatecznie zmodyfikowanej listy.

Podsumowując:

    zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
    znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
    policz średnią z ostatecznie zmodyfikowanej listy numbers i przypisz ją do zmiennej mean_number
    """
numbers = [5,32,56,2,2,16,7,10,23,100]
#srednia z modyfikacji
mean_number = 0
#raound up numbers
for index, number in enumerate(numbers):
    if number == 5:
        numbers[index] = 10
    else:
        numbers[index] = round(number/10)*10
print(numbers)
#remove min&max
numbers.remove(max(numbers))
numbers.remove(min(numbers))
print(numbers)
#median
mean_number = sum(numbers)/len(numbers)
print(mean_number)