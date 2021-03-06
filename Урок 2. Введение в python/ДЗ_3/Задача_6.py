'''
В первой строке содержится целое число N (1 <= N <= 10^9). Последовательность
чисел Фибоначчи задается следующим образом: F[1] = 1. F[2] = 1.
F[k] = F[k - 1] + F[k - 2] для k >= 3. Определить, является ли N числом
Фибоначчи. Если является, то вывести "True", если нет – вывести "False".
'''

n = int(input())
f1 = 1
f2 = 1

while f2 <= n:
    if f2 == n:
        print('True')
        break
    f1, f2 = f2, f1 + f2
else:
    print('False')
