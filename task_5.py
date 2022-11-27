#Реализуйте алгоритм перемешивания списка.
#Из библиотеки random использовать можно только randint

import random
length = int(input('Введите длину списка: '))
lst = [random.randint(-10,10) for i in range(length)]
print(lst)
for j in range(len(lst)):
    index_rand = random.randint(0, len(lst) - 1)
    temp = lst[j]
    lst[j] = lst[index_rand]
    lst[index_rand] = temp
print(lst)








'''
import random
length = int(input('Введите длину списка: '))
lst = [random.randint(-10,15) for i in range(length)]
print(lst)
for j in range(len(lst) - 1):
    lst[j], lst[j + 1] = lst[j + 1], lst[j]
    lst[j], lst[len(lst) - 1] = lst[len(lst) - 1], lst[j]
    lst[j + 1], lst[len(lst) - 2] = lst[len(lst) - 2],  lst[j + 1]
    
print(lst)
'''