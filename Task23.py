# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

size = int(input('Введите размер списка: '))
list1 = []
for i in range(size):
    n = int(input('Введите число: '))
    list1.append(n)
print(*list1)

list2 = []
for i in range(len(list1)):
    while i < len(list1) / 2 and size > len(list1) /2:
        size -= 1
        m = list1[i] * list1[size]
        list2.append(m)
        i += 1
print(*list2)
