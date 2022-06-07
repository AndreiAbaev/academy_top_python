'''
Напишите программу, которая вычисляет значение выражения по формуле: ...
В первой строке содержится натуральное число n (1 <= n <= 15) Вывести результат
с точностью 0.000001
'''

n = int(input())
total = 0

for i in range(1, n + 1):
    numerator = 1
    denominator = 0
    
    for j in range(1, i + 1):
        numerator *= j
        denominator += 1 / (j + 1)
    
    total += numerator / denominator
    
print(round(total, 6))
