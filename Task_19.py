''' Задача 19 Дана последовательность из N целых чисел и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
K – положительное число.
Input:   [1, 2, 3, 4, 5] k = 3
Output:  [3, 4, 5, 1, 2]'''

# 1 вариант
# lst_1 = [1, 2, 3, 4, 5]
# lst_2 = list()
# k = 2
# for i in range(len(lst_1) - k):
#     print(lst_1[i])
#     lst_2.append(lst_1.pop(0)) #удаляем из lst_1 элемент и добавляем его в lst_2
# print(lst_1 + lst_2)

# 2 вариатн
lst_1 = [1, 2, 3, 4, 5]
k = int(input("Введите колличество сдвигов: ")) % len(lst_1)
if k == 0:
    print(lst_1)
else:
    print(lst_1[- k:] + lst_1[:len(lst_1) - k])