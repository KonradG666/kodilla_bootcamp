shoping_list = {"Piekarnia": ["Chleb", "bułki", "Pączek"], "Warzywniak": ["Marchew", "Seler", "Rokula"]}

for shop, item in shoping_list.items():
    print(f"Idę do {shop} i kupuję tam: {item}")
    
count = 0
for shop, item in shoping_list.items():
    if isinstance(item, list):
        count += len(item)
print(f"W sumie kupuję {count} produktów.")

#print(f"W sumie kupuję {sum([len(shoping_list[x]) for x in shoping_list if isinstance(shoping_list[x], list)])} produktów.")