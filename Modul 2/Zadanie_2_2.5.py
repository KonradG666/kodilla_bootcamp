number_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
print(f"Pełna Lista: {number_list}")
zero = number_list[1:4] + number_list[5:10] + number_list[12:14]
print(f"Same zera: {zero}")
numbers = number_list[0:5:4] + number_list[10:12]
print(f"Tylko liczby: {numbers}")