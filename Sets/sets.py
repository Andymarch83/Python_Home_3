"""
Задача 22: Даны два неупорядоченных набора целых чисел
(может быть, с повторениями). Выдать без повторений в
порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого
множества. m — кол-во элементов второго множества. Затем
пользователь вводит сами элементы множеств.
"""
# from random import randint

# set_n = list(randint(1, 10) for i in range(int(input('Введите количество элементов множества n: '))))
n = int(input('Введите количество элементов множества n: '))
set_n = []
for i in range(n):
    s = int(input())
    set_n.append(s)

# set_m = list(randint(1, 10) for i in range(int(input('Введите количество элементов множества m: '))))
m = int(input('Введите количество элементов множества m: '))
set_m = []
for i in range(m):
    t = int(input())
    set_m.append(t)

print(set_n)
print(set_m)

set_n = set(set_n)
set_m = set(set_m)
s_set = list(set_n.intersection(set_m))

print(s_set)
