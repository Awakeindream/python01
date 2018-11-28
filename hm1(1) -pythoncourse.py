#  Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


number = int(input('Enter a number '))
i = 0
while i < len(number):
print(number[i])
i += 1
print("The programm has been successfully executed")
	
	
#or ***to complete***
number = int(input('Enter a number '))
for i in number:
i = 0
    print(number[i])
	i += 1
print("The programm has been successfully executed")
	
    

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print("a = " , a, " b = " , b)
a,b = b,a
print(" a = ", a, " b = ", b)

#or

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
print("a = " , a, " b = " , b)
c = a
print("c = " , b, " b = " , c)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

user_age = "18"
permission = int(input("Enter your age: "))
if permission >= int(user_age):
    print("You are welcome to use our service")
else:
    print("Sorry, the service is not avaliable for people under 18")

#or
user_age = int(input("Enter your age: "))
if user_age < 18:
    access = False
    print("Sorry, the service is not avaliable for people under 18")
	
else:
    access = True	
    print("You are welcome to use our service")
    
	
	
	
# homework/ normal

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

x = 98765
print("Max number in the string" , x, end = " ")
max_number = 9
while True:
    if max_number = 9:
        break
else:
        continue
    print(max_number)
	max_number +=1


#or

x = 98765
print("Max number in the string" , x, end = " ")
max_number = 9
max_number = str(x)
for digit in x:
print(digit)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
   

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
a = b
b = a
print(a,b)
  
# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax** + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

ax** + bx + c = 0


 a = int(input("Enter number for a "))
 x = int(input("Enter number for x"))
 b = int(input("Enter number for b"))
 c = int(input("Enter number for c"))
 
 








# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось? 

bool True False
bool= False if
bool (0)
bool (' ')
bool (False)

# Для всех остальны значений a > 999999  bool = True
 

	
