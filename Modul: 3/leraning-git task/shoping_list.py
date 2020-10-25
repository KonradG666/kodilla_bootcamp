#your shopping list
shoping_list = {"Piekarnia": ["Chleb", "bułki", "Pączek"], "Warzywniak": ["Marchew", "Seler", "Rokula"]}
#list to upper case
upper_list = {k.upper():[i.upper() for i in v] for k,v in shoping_list.items()}
#print lists
for shop, item in upper_list.items():
    print(f"Idę do {shop} i kupuję tam: {item}")
#count items on the list  && print 
count = 0
for shop, item in shoping_list.items():
    if isinstance(item, list):
        count += len(item)
print(f"W sumie kupuję {count} produktów.")
