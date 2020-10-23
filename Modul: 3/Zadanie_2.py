by_5 = []
by_3 = []
for num in range(0,100):
    if num % 5 == 0:
        by_5.append(num)
    elif num % 3 == 0:
        by_3.append(num)

print(f"Liczby podzielen przez 5: {by_5}".format(by_5))
print(f"Liczby podzielne przez 3: {by_3}".format(by_3))