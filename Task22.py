# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

list = []
for i in range(5):
    n = int(input('Введите число: '))
    list.append(n)
print(*list)

s = 0
for i in range(len(list)):
    if i % 2 == 1:
        s += list[i]
print(f"Сумма равна: {s}")