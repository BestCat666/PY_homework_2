#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

num = int(input('Введите число: ')) 
lst = [i + 1 for i in range(-num - 1, num)]
print(lst)
pos_1 = int(input('Введите позицию первого элемента: ')) 
pos_2 = int(input('Введите позицию второго элемента: ')) 
mult = lst[pos_1] * lst[pos_2]
print('произвдение элементов на указанных позициях = ', mult)