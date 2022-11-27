#lst = [i for i in range(1, num + 1)]

# lst = [0 for i in range(7)]
#print(lst)

# lst = [i for i in range(10)] от 0 до 9
#print(lst)

# lst = [i**2 for i in range(10)] квадраты от 0 до 9
#print(lst)

# lst = [i for i in 'hello']
#print(lst)

#lst = input().split()
#lst[int(i) for i in lst]
#print(lst)

''' 
отдельно для дробного
num = input('Введите число: ')   # тип данных str
num_split = num.split('.')
a = int(num_split[0]) # целая чаcть
b = int(num_split[1]) # дробная чаcть
sum = 0
while a > 0:
    last_a = a % 10
    sum = sum + last_a
    a = a // 10
while b > 0:
    last_b = b % 10
    sum = sum + last_b
    b = b // 10
print('Сумма всех цифр в числе: ', sum)

отдельно для целого
num = int(input('Введите число: '))  
sum = 0
while num > 0:
    last = num % 10
    sum = sum + last
    num = num // 10
print('Сумма всех цифр в числе: ', sum)
'''






