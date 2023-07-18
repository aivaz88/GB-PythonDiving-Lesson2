# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions
from math import gcd

fr_1 = input('Введите дробь в формате "a/b": ')
fr_2 = input('Введите дробь в формате "a/b": ')

a = int(fr_1[0])
b = int(fr_1[2])
c = int(fr_2[0])
d = int(fr_2[2])
fr_1 = fractions.Fraction(a, b)
fr_2 = fractions.Fraction(c, d)
print('Расчет с помощью функции:')
print(fr_1, '+', fr_2, '=', fr_1+fr_2)
print(fr_1, '*', fr_2, '=', fr_1*fr_2)
print('Расчет руками:')
x = gcd(a, b)
a /= x
b /= x
x = gcd(c, d)
c /= x
d /= x
x = str((a * d) + (c * b))
y = str(b * d)
print(fr_1, '+', fr_2, '=', x+'/'+y)
x = str(a * c)
y = str(b * d)
print(fr_1, '*', fr_2, '=', x+'/'+y)