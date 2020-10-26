#your shopping list
shoping_list = {"Piekarnia": ["Chleb", "Bułki", "Pączek"], "Warzywniak": ["Marchew", "Seler", "Rokula"]}
#list to upper case
upper_list = {k.upper():[i.upper() for i in v] for k,v in shoping_list.items()}
#print shopping lists for each shop
for shop, item in upper_list.items():
    print(f"Idę do {shop} i kupuję tam: {item}")
#count number of shops & print
print(f"Idę do:",(len(shoping_list)),"sklepów")
#count number of items & print
count = sum([len(shoping_list[shop]) for shop in shoping_list if isinstance(shoping_list[shop], list)])
print(f"W sumie kupuję {count} produktów.")
