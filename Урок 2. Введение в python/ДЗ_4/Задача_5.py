'''
Дано натуральное n. Вычислить сумму членов ряда по формуле: ...
В первой строке содержится целое число n (1 <= n <= 100). - количество членов
ряда. Вывести сумму членов ряда с точностью 0.000001.
'''

n = int(input())
total = 0

for i in range(1, n + 1):
    total += 1 / (2 * i) ** 2
    
print(round(total, 6))
