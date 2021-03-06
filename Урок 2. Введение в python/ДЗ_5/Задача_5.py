'''
Дана последовательность из n целых чисел, каждое из которых находится в диапазоне от 0 до 100.
Указать в данной последовательности количество вхождений числа, встречающегося чаще других.

Формат ввода:
В первой строке ввода содержится число n, в следующей – последовательность чисел, разделённых пробелом.

Формат вывода:
Количество вхождений числа, встречающегося чаще других.

Пример ввода:

5
1 3 2 4 1
Пример вывода:

2
'''

n = input()
a = [int(i) for i in input().split()]
frequency = [0 for _ in range(101)]

for i in a:
    frequency[i] += 1

print(max(frequency))
