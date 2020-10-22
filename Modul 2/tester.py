my_list = range(3,1000)
print(f"Lista liczb to: {my_list}")

new_list = []

for num in my_list:
    for i in range(3, num):

        if num % 3 != 0:
            break
        else:
            new_list.append(num)
    while num < 100:
        break

print(f"Liczby pierwsze: {new_list}")
