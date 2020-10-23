num_list = range(1,11)
print(num_list)
cube_list = [num*num*num for num in num_list]
print(cube_list)
nd = []
for num in cube_list:
  if num %2 != 0:
    nd.append(num)
  else:
    pass
print(nd)