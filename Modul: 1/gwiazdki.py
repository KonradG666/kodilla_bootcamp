# Nr 1
print("* " * 10)
for i in range(2, 6):
    print("* " * 10)
    print(" *" * 10)
print("* " * 10)

# Nr 2
for i in range(1, 5):
    if i // 2 == 0:
        print("**" * i)
        print("**" * i)
    elif i // 2 != 0:
        print("**" * i)
        print("**" * i)
    else:
        pass

# Nr 3
for a in range(6, 0, -1):
    if a > 1:
        print("*" * a)
    elif a == 1:
        print("*" * a)
    else:
        pass

