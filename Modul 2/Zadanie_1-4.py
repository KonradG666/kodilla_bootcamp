print("Zadanie Nr.1\n")
name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
print(name_list)
name_dictionary = {"John": 4, "Michael": 7, "Terry": 5, "Eric": 4, "Graham": 6}
print(name_dictionary)
print("\n")

# print("Zadanie Nr.2\n")
# my_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
# print(f"Lista liczb to: {my_list}")

# new_list=[]
# for num in my_list:
#  for i in range(2,num):
#    if num % i == 0 or num == 1:
#      break    
#  else:
#    new_list.append(num)

# print(f"Liczby pierwsze: {new_list}")
# print("\n")

print("Zadanie Nr.3")
week = ['pon', 'śro', 'pią', 'sob']
print(week)
week.insert(1, "wto")
week.insert(3, "czw")
week.insert(6, "nie")

print(week)
print("\n")

print("Zadanie Nr.4")
making_tea = ["włącz czajnik", "znajdź opakowanie herbaty", "zalej herbatę", "nalej wody do czajnika", "wyjmij kubek",
              "włóż herbatę do kubka"]
print(f"Not sorted tea making instructions: \n {making_tea}")
print("\n")

print("Tea making instructions.")
print(making_tea[3])
print('\n'.join(making_tea[0:5]))
print(making_tea[2])
