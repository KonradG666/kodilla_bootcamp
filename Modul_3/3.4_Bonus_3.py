"""
Twojemu szefowi udało się znaleźć informacje o najlepiej sprzedających się modelach samochodów w 2018 roku. Dane, które zdobył nie nadają się niestety 
do analizy, dlatego poprosił Cię o przetworzenie, aby można było z nich w prosty sposób wyciągać informacje.

Do zmiennej models przypisano listę zawierającą najlepiej sprzedające się samochody 2018 roku uszeregowane od najlepiej sprzedającego się w formacie 
'producent - model'.
Do zmiennych sales2018, sales2017 oraz sales2016 przypisano liczbę sprzedanych egzemplarzy tych modeli kolejno w roku 2018, 2017 oraz 2016.

Czyli - najlepiej sprzedającym się modelem samochodu w 2018 roku był: Volkswagen Golf (pierwsza pozycja na liście models). Golf w 2018 roku sprzedał się 
w ilości 445 754 egzemplarzy (pierwsza pozycja na liście sales2018). Wiemy też, że w 2017 roku sprzedano 483 105 modeli Golfa (pierwsza pozycja na liście 
sales2017), oraz że w 2016 roku sprzedano 492 952 egzemplarzy Golfa (pierwsza pozycja na liście sales2016).

Niektóre samochody nie były sprzedawane przed 2018 rokiem. W takim przypadku dane o ich sprzedaży zastąpione są wartością 'NA'. 
Zastąp wszystkie 'NA' cyfrą 0.

Na podstawie otrzymanych danych zbuduj słownik o następującej strukturze i przypisz go do zmiennej cars:

cars = {"brand": {"model1":{"sales":{"2016": 123,

                                     "2017": 456,

                                     "2018": 789}},

                  "model2":{"sales":{"2016": 987,

                                     "2017": 654,

                                     "2018": 321}}

                 },

        "brand2": ... }


Czyli na przykładzie rzeczywistych danych powinien wyglądać on następująco:

cars = {"Opel": {"Corsa":{"sales":{"2016": 264844,

                                   "2017": 232738,

                                   "2018": 217036}},

                 "Astra":{"sales":{"2016": 253483,

                                   "2017": 217813,

                                   "2018": 160275}}

                 },

        "Dacia": ... }



Następnie postaraj się odpowiedzieć na pytania zaprezentowane poniżej:

    Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej answer1.
    Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej answer2.
    Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej answer3.
    Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej answer4.
    O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej answer5. Odpowiedź podaj w formacie procentowym jako string. Np. '21%'.


UWAGA! Na potrzeby zadania potraktuj 'VW' i 'Volkswagen' jako osobnych producentów
"""
models = ['Volkswagen - Golf','Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','336,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','327,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']

answer1 = "" # wskaż nazwę modelu jako string
answer2 = "" # wskaż producenta jako string
answer3 = [] # wskaż odpowiedź jako listę zawierającą wszystkie modele spełniające kryteria
answer4 = "" # wskaż nazwę modelu jako string
answer5 = "" # odpowiedź podaj w formacie procentowym jako string. Np. '21%'

cars = {}
car =[]
brand = []
for index, item  in enumerate(sales2017):
    if item == 'NA':
        sales2017[index] = 0
for index, item  in enumerate(sales2016):
    if item == 'NA':
        sales2016[index] = 0


print("----------------------------")
for index, row in enumerate(models):
    print(index)
    print((row.split(" - ")))
    print(sales2018[index])    
    print(sales2017[index])
    print(sales2016[index])
    car.append(((row.split(" - "))))
print("----------------------------")
for b, m in car:
    brand.append(b)
brand = set(brand)
cars = brand

cars = brand

for car[0][0] in brand:
    if car[0][0] == brand[0]:
        brand[0].append(set(car[0][1])
#sales2016[0]

#print(car)


#for car in cars:
#    first_letter = name[0]
#    # if letter in append the name
#    if first_letter in name_dict:
#        name_dict[first_letter].append(name)
    # if letter not in create new and append
#    else:
#        name_dict[first_letter] = [name]

print(cars)
print(brand)
print("----------------------------")

cars = {car[0][0]: {car[0][1]:{"Sales":{"2016": str(sales2016[0]),

                                     "2017": str(sales2017[0]),

                                     "2018": str(sales2018[0])}},

                  car[2][1]:{"sales":{"2016": 987,

                                     "2017": 654,

                                     "2018": 321}}

                 },

        "brand2": ... }

print(cars)