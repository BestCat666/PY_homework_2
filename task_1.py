#1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#*Пример:*
#6782 -> 23
#0.56 -> 11

num = input('Введите число: ')   # тип данных str
num = int(num.replace('.', ''))  
sum = 0
while num != 0:
    last = num % 10
    sum = sum + last
    num = num // 10
print('Сумма всех цифр в числе: ', sum)




