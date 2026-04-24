numeros = [-1, 1, -2, -3, 7, 10]

num_posi = 0
num_nega = 0
total = 0

for num in numeros:
    total += num
    if num > 0:
        num_posi += 1
    elif num < 0:
        num_nega += 1

print(num_posi)
print(num_nega)
print(total)