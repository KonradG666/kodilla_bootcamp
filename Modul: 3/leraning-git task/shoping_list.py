#your shopping list
shoping_list = {"Piekarnia": ["Chleb", "bułki", "Pączek"], "Warzywniak": ["Marchew", "Seler", "Rokula"]}
#uppercase list
#upper_list = ((k.upper(), v.upper()) for k, v in shoping_list.items())
#print lists
for shop, item in shoping_list.items():
    print(f"Idę do {shop.upper()} i kupuję tam: {item}")
#count items on the list  
count = 0
for shop, item in shoping_list.items():
    if isinstance(item, list):
        count += len(item)
print(f"W sumie kupuję {count} produktów.")