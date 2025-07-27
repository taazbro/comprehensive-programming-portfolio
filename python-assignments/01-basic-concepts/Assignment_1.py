#numbers from 0 to 6 except 3 and 6
for numbers in range(6):
    if (numbers == 3 or numbers==6):
        continue
    print(numbers,end=' ')
print("\n")