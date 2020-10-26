my_list = []

for num in range(1000):
    divi = num % 3
    # while loop
    if divi == 0:
        my_list.append(num)
    # break out of loop
    elif num > 100:
        break
print(my_list)
