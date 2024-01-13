import random

'''
1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
# def create_list(a):
#     a_list = []
#     for i in range(a):
#         a_list.append(random.randint(1, 99))
#     return a_list
#
#
# digit_count = int(input('Enter the number of digit: '))
# my_list = create_list(digit_count)
# res_list = []
# for i in range(len(my_list) - 2):
#     if i % 2 != 0:
#         res_list.append(my_list[i] * my_list[i + 2])
# print(f'{my_list} -> {res_list}')
'''
2) Написать программу, которая генерирует двумерный массив 
на A x B элементов ( A и B вводим с клавиатуры)
И считаем средне-арифметическое каждой строки (не пользуемся 
встроенными методами подсчета суммы)
'''
# num_a = int(input('Enter the number of columns: ')) # Количество колонок
# num_b = int(input('Enter the number of row: ')) # Количество строк
#
# dim_list = [[random.randint(1, 101) for _ in range(num_a)] for _ in range(num_b)] # Создание двумерного массива
# print(dim_list)
# res_list = []
# for i in range(num_b): # Спедне-арифметичемкое строки
#     tmp = 0
#     for j in range(num_a):
#         tmp += dim_list[i][j]
#     tmp /= num_a
#     res_list.append(tmp)
# print(res_list)
'''
Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
'''
def selection_sort(alist):
    for i in range(len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i]

my_list = [random.randint(1, 101) for i in range(30)]
print(my_list)
selection_sort(my_list)
print(my_list)
