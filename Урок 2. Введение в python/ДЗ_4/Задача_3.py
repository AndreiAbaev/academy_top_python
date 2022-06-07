'''
Даны два целых числа a и b. Найти сумму квадратов чисел от a до b включительно.
'''

a, b = (int(i) for i in input().split())
total = 0

for i in range(a, b + 1):
    total += i**2
    
print(total)
