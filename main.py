# LESSON 1
# import random

# name = "Elena"  # инициализация переменной
# print("Hello,", name)

# age = 20
# text = "Hello"
# print(text + str(age))
# print(type(age))

# LESSON 2

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num += 5
# print(num)
#
# num -= 3
# print(num)

# num = 4325
# print("Исходное число: ", num)
# a = num % 10
# print(a)
# num //= 10
#
# b = num % 10
# print(b)
# num //= 10
#
# c = num % 10
# print(c)
# num //= 10
# print(num)

# num = 4325
# print("Исходное число: ", num)
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = '2.3'
# num2 = 3
# # # res = num1 + str(num2)
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.891, 2))
# print(type(round(3.8424, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", str(age), " лет.", sep="", end=" ")
# print("Я учу Python")

# name = input("Напиши имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# print(bool("python"))
# print(bool(""))
# print(bool(-0.2))
# print(bool(0))

# print(7 == 7)
# print(2 + 5 == 7)
# print(7 != 10 - 7)

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 < 4)

# print(9 - 7)
# print(not 9 - 7)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# a = 15
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# elif a == b == c:
#     print("Треугольник равносторонний")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день - ")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# else:
#     print("Такого дня не существует")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:
#         print("ворон")
#
# else:
#     print("Ошибка ввода данных")


# password = "qwerty"
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 15
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 13 or 15 <= time <= 16:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
#
# print(a if a < b else b)

# a, b = 20, 30
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 5
# b = 1
# print("на ноль делить нельзя" if b == 0 else a / b)
# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполниться в любом случае
#     print("Конец программы")


# n = input("Введите первое число:")
# m = input("Введите второе число:")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы
# while

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Введите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i +=1
# print("*" * n)

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# summ = 0
# while a <= b:
#     if a % 2:
#         summ += a
#     a += 1
# print(summ)

# n = int(input("Введите количество символов: "))
# symbol = input("Тип символа: ")
# orient = int(input("0 - горизонтальная\n1 - вертикальная\n ориентация линии: "))
# i = 0
# while i < n:
#     if orient == 0:
#         print(symbol, end=' ')
#     if orient == 1:
#         print(symbol)
#     i += 1


# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершен")

# i = 0
# while True:
#     n = int(input("Введите положительное число:"))
#     i += 1
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен, i=", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\t Внутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j , end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*")
#     i += 1

# for i in "Hello!":
#     print(i)

# for i in range(2,9):
#     print(i)

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++ i =", i)
#     for j in range(2):
#         print("----- j =", j)

# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()
#
# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter for letter in "Banana"]
# print(nums)

# nums = [i for i in range(30) if i % 2 == 0]
# print(nums)

# Список (list)
# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# for i in range(len(nums)):
#     print(i)

# s = []
# print(s)
#
# b = list("Hello")
# print(b)

# n = list(range(1, 6, 2))
# print(n)


# [выражение for переменная in последовательность]

# a =[0 for i in range(5)]
# print(a)
# b =[i for i in range(5)]
# print(b)
#
# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [input() for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)
# j = 0
# for i in a:
#     if i < 0:
#         j += i
# print(j)

# a = list(range(10, 200, 10))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
#
# for i in a:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]

# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print(k)
# print("sum нечетных элементов: ", s)

# a = [int(input()) for i in range(int(input("Введите количество элементов списка: ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# a = [7, 8, 2, 1, 17, 9]
# print(a)
# # a[0], a[1] = a[1], a[0]
# # print(a)
# print(a[1:4])
# print(a[1:])
# print(a[:3])
# print(a[::-1])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# Методы списков
# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет элемент (второй параметр), в заданный индекс (первый параметр)
# print(s)
# s = []
# n = int(input("Кол0во элементов в списке: "))
# for num in range(n):
#     while True:
#         x = int(input("Введите число:"))
#         if x % 3 == 0:
#             s.insert(0, x)
#             break
#         else:
#             print(x, "не кратное 3")
# print(s)

# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
#
# print(s)
#
# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.append(x)
# a = int(input("Введите индекс: "))
# s.pop(a)
#
# print(s)
#
# a = [1, 2, 3]
# b = a.copy()
# a.append(20)
# print(a, b)
# b.append(120)
# print(a, b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# b = ["Виталий", "Сергей", "Александр", "Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# sort = sorted(a, reverse=True)
# print(sort)

# Генерация случайных данных
# import random
#
# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9))
# print(random.uniform(10.5, 25.5))
# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# # print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)

# import random
# mas = [random.randint(0, 20) for i in range(10)]
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)
# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# min_ch = min(mas)
# print(min_ch)
#
# ind_min = mas.index(min_ch)
# print(ind_min)
# del mas[:ind_min]
# print(mas)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
#
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# import random
# w, h = 4, 3
# matrix = [[random.randint(1,30) for x in range(w)]for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# import random
# w, h = 3, 4
# matrix = [[random.randint(-20,10) for x in range(w)]for y in range(h)]
#
# m = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             m += 1
#     print()
#
# print("Количество отрицательных элементов:", m)

# for x, y in [[1,2], [3,4], [5,6], [7,8]]:
#     print(x, "+", y, "=", x + y)

# import math as m
# from math import *
# num1 = sqrt(4)
# print(num1)

# import time
# seconds = time.time()
# print("Количество секунд", seconds)
# locale_time = time.ctime()
# print("Местное время:", locale_time)

# Function

# def hello():
#     print("Hello")
# hello()


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(1, 5, d=n4))


# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, '*')
# set_param(s="#")


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         elif not even and current % 2:
#             s += current
#         n //= 10
#     return s
#
#
# print("\nСумма четных цифр: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр: ")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# n = 5
# print(id(n))
# n = 6
# print(id(n))

# n = [1, 2, 3]
# print(id(n))
#
# n.append(4)
# print(n)
# print(id(n))

# Кортеж(tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())


# a = (5,)
# print(type(a))
# print(a)
# b = tuple()
# print(type(b))

# n = [1, 2, 3]
# b = tuple(("Hello", "Python"))
# print(type(b))
# print(b)

# a = (1, 2, 3, 4, 5, 6)
#
# print(a[3])
# print(a[1:3])

# from random import randint
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# tpl = tuple(2 ** i for i in range(1, 13))
# print(tpl)

# t1 = tuple("hello")
# t2 = tuple('world')
# print(t1)
# print(t2)
# # print(t1 * 2)
# t3 = t1 + t2
# print(t3.)


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             a = tpl.index(el)
#             b = tpl.index(el, a+1)
#             return tpl[a:b + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)


# print("Вносим изменения")

# print("Склонированный репозиторий")

# Множества (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)

# c = ["red", "blue", "green", "red"]
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
# s = {x for x in mas}
# print(s)

#
# def to_set(elem):
#     return set(elem), len(elem)
#
#
# print(to_set("я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = ["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {'Tom', 'Bob', 'Alice'}
# print(a)
# a.add('Ann')
# print(a)
# a.remove("Ann")  # при обращении к несуществующему элементу - ошибка KeyError
# print(a)
# user = "Ann"
# if user in a:
#     a.remove(user)
# print(a)


# a.discard("Ann")
# n = a.pop()
# print(n)
# a.pop()
# a.clear()
# print(a)
# print(n)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # # c = a | b
# # a |= b
# # print(a)
#
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7,8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
#
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
#
# both_hobbies = drawing & music
# print("Оба кружка", both_hobbies)
#
# drawing -= both_hobbies
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)


# Тип frozenset
# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"hello", "world"})

# Словарь (dict)
# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3, 4: 'four'}
# lst[0] = 10
# print(lst[0])
#
# d['one'] = 10
# print(d['one'])
# print(d[4])

# d = {}
# print(d)
# print(type(d))
# d1 = dict(one=1, two=2)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# m = 1
# for i in d:
#     m *= d[i]
#
# print(m)


# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400],
# }
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Количество: '))
#     try:
#         goods[n][1] = qty
#     except KeyError:
#         pass
#     else:
#         break
#
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], " шт. по ", goods[i][2], 'руб', sep="")


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# item = d.popitem()
# print(item)


# Задание 1
# vowels = set('аеёиоуыэюя')
# message = input("Введите строку: ")
# count = 0
# for i in message:
#     if i in vowels:
#         count += 1
# print("Количество гласных равно: ", count)


# Задание 2
# dict1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# dict2 = {'name': dict1.pop('name'), 'salary': dict1.pop('salary')}
# print(dict1)
# print(dict2)

# d = {'a': 1, 'c': 3, 'b': 2}
# d1 = {'r': 7, 'q': 40}
# d. update(d1)
# d2 = [('a', 20), ('b', 9)]
# d.update(d2)
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# # z.update(x)
# # z.update(y)
# print(z)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep='')


# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep='')

# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
#
# sales[person][region] = new_data
# print(sales[person])


# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# d = {value: key for key, value in d.items()}
# print(d)


# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# new_d = {k: v for k, v in d.items() if v <= 2}
# print(new_d)

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()
# current_key = ""
# for item in a:
#
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
#
# print(d)

# d = dict(zip([1, 2, 3, 4], ['one', 'two', 'three']))
# print(d)
#
# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# f = {k: v for k, v in zip(a, b)}
# print(f)


# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в", m, "=", profit)


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))


# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def num(*args):
#     res = 0
#     for i in args:
#         res += i
#     c = res / len(args)
#     for i in args:
#         if i < c:
#             print(i)
#
#
# print(num(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(num(3, 6, 1, 9, 5))


#
# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(d=9))


# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print('a:', a)
#     fun2(4)
#
#
# fun1()
# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a:", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)
# x = 5
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item1(1))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res1()


# lambda(анонимные функции)

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
# for i in y:
#     print(i('abc__'))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: + n
# f2 = outer2(5)
# print(f1(10))
#
# print((lambda n: lambda x: x + n)(5)(10))


# func = (lambda a, b, c: a + b + c)
# print(func(2, 4, 5))


# d = {'b': 3, 'c': 1, 'a': 2}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d1 = dict(lst)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9}
# ]

# a = [
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y
# ]
#
# print(a[0](5, 2))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[6]()


# print((lambda a, b, c: a if (a < b and a < c) else b if (b < c and b < a) else c)(15, 13, 1))


# 1

# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for t, p, m in zip(total_sales, prod_cost, month):
#     print("Общая прибыль в", m, "=", t - p)

# 2

# n = int(input("Количество студентов: "))
# data = dict()
# for i in range(n):
#     name = input(f'{i + 1}-й студент: ')
#     numb = int(input("Балл: "))
#     a = {name: numb}
#     data.update(a)
# 
# 
# def func(args):
#     middle = sum(args) // len(args)
#     print(middle)
#     for k, v in data.items():
#         if v > middle:
#             print(k)
#     res = []
#     for element in args:
#         if element > middle:
#             res.append(element)
#     return res
# 
# 
# f = func(data.values())


import math

d = {
    'circle': lambda x: math.pi * x * x,
    'rectangle': lambda x, y: x * y,
    'trapezoid': lambda x, y, z: (x + y) * z / 2
}
print("Площадь окружности:", d['circle'](2))
print("Площадь прямоугольника:", d['rectangle'](10, 13))
print("Площадь трапеции:", d['trapezoid'](7, 5, 3))
