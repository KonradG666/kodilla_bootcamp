num = 30
fibonacci = []
a = 0
b = 1
# fibonacci.append(a)
fibonacci.append(b)
for i in range(0, 29):
    c = a + b
    a = b
    b = c
    fibonacci.append(c)
print(fibonacci)
print("")
print(sum(fibonacci))
