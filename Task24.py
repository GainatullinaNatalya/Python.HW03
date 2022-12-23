# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# list1 = input().split()
# list2 = []
# for i in list1:
#
#     if point in i:
#
#         list2.append(list1[i + 1:-1])
# print(*list2)

list1 = []
for i in range(5):
    n = float(input('Введите число: '))
    list1.append(n)
print(*list1)

list2 = []
for i in list1:
    find = i - int(i)
    list2.append(find)
res = str(max(list2) - min(list2))
print(res[:4])