lista_zakupów = {"Piekarnia": ["Chleb", "bułki", "Pączek"], "Warzywniak": ["Marchew", "Seler", "Rokula"]}

for shop, item in lista_zakupów.items():
    print(f"Idę do {shop} i kupuję tam: {item}".format(shop,item))
    
count = 0
for shop, item in lista_zakupów.items():
    if isinstance(item, list):
        count += len(item)
print(f"W sumie kupuję {count} produktów.".format(count))