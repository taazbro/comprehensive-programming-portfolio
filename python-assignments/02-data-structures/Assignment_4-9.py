cubes = []
#print list of the first 10 cubes
for number in range(1, 10):
    cube = number**3
    cubes.append(cube)

#print The first three items of the cubes
print(cubes[0:3])
#print Three items from the middle of the cubes
print(cubes[3:6])
#print The last three items in the cubes
print(cubes[6:])