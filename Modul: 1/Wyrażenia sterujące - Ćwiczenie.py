
num_list = 0
#Define a for loop 
for x in range(1, 1000):
    if x % 6 == 0:
        print(x)
        num_list += 1
    else:
        if num_list == 30:
            break

print(" ")
print(" ")

n = 1
counter = 0
while True:
  if n % 6 == 0:
    print(n)
    counter += 1
    if counter == 30:
      break


  n +=1


