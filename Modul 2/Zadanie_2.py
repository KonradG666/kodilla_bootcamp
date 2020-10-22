print("Zadanie Nr.2\n")
my_list = [0, 1, 2, 3, 5, 6, 11, 12, 18, 19, 21]
print(f"Lista liczb to: {my_list}")

new_list = []

for num in my_list:
    if num <= 1:
        continue
    for i in range(2, num):
        if num % i == 0 or num == 1:
            break
    else:
        new_list.append(num)

print(f"Liczby pierwsze: {new_list}")
print("\n")
