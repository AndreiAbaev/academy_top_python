'''
Есть две коробки, первая размером A1×B1×C1, вторая размером A2×B2×C2.
Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
что поворачивать коробки можно только на 90 градусов вокруг ребер.

Формат входных данных
Программа получает на вход числа A1, B1, C1, A2, B2, C2.

Формат выходных данных
Программа должна вывести одну из следующих строчек: Boxes are equal, если
коробки одинаковые, The first box is smaller than the second one, если первая
коробка может быть положена во вторую, The first box is larger than the second
one, если вторая коробка может быть положена в первую, Boxes are incomparable,
во всех остальных случаях.
'''

a1, b1, c1, a2, b2, c2 = (int(input()) for _ in range(6))

if a1 == a2 and b1 == b2 and c1 == c2 or \
    a1 == a2 and b1 == c2 and c1 == b2 or \
    a1 == c2 and b1 == b2 and c1 == a2 or \
    a1 == b2 and b1 == a2 and c1 == c2 or \
    a1 == b2 and b1 == c2 and c1 == a2 or \
    a1 == c2 and b1 == a2 and c1 == b2:
    print('Boxes are equal')
elif a1 <= a2 and b1 <= b2 and c1 <= c2 or \
    a1 <= a2 and b1 <= c2 and c1 <= b2 or \
    a1 <= c2 and b1 <= b2 and c1 <= a2 or \
    a1 <= b2 and b1 <= a2 and c1 <= c2 or \
    a1 <= b2 and b1 <= c2 and c1 <= a2 or \
    a1 <= c2 and b1 <= a2 and c1 <= b2:
    print('The first box is smaller than the second one')
elif a1 >= a2 and b1 >= b2 and c1 >= c2 or \
    a1 >= a2 and b1 >= c2 and c1 >= b2 or \
    a1 >= c2 and b1 >= b2 and c1 >= a2 or \
    a1 >= b2 and b1 >= a2 and c1 >= c2 or \
    a1 >= b2 and b1 >= c2 and c1 >= a2 or \
    a1 >= c2 and b1 >= a2 and c1 >= b2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
