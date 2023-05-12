'''
import math
def func(x):
    return math.sqrt((55*(69 * x**3 + 2 * x**2 + 1)**4 - 7)
                     //(15*(2 * x + 73 + 75 * x**2) +
                        52*(1 - 42 * x**3 - 62 * x)**2)) + 59*(54 * x - 29)**5

print(func(-0.69))
''''''
def func(z):
    if z < -36:
        return z**5
    if z >= 13:
        return (87*z**3)**4 /95 -74*(78*z +z**2 +z**3)**7
    else:
        return 96*(1 - 97*z**3)

print(func(-28))
''''''
import math

def func(b, n, y):
    a = 0
    for j in range(1, b + 1):
        a += (math.log2(j**3 / 80))**6 - (78 * j**3 - 58 * j**2)**5
    for j in range(1, n + 1):
        c = 1
        for i in range(1, b + 1):
            c *= (4 * y**2 + 0.02 + 25 * i**3)**4 - 1 - 97 * j**2
        a += c
    return a

print(func(8, 7, 0.39))
''''''
import math

def func(n):
    if n == 0:
        return 0.44
    else:
        return func(n - 1) - (abs(func(n - 1)))**3 / 57

print(func(4))
''''''
import math

def func(x):
    a = 0
    for i in range(1, 6):
        a += (6 * (x[5 - math.ceil(i/3)])**2 - 58 * (x[5 - i])**3 - 36)**7
    return a


print(func([0.89, -0.67, 0.79, 0.61, -0.15]))
''''''
def func(x):
    match x[3]:
        case 2018:
            match x[0]:
                case 'D':
                    match x[1]:
                        case 1960:
                            return 0
                        case 2009:
                            match x[2]:
                                case 'HAML':
                                    return 1
                                case 'C++':
                                    return 2
                                case 'SCAML':
                                    return 3
                        case 1976:
                            return 4
                case 'LEAN':
                    return 5
                case 'YANG':
                    match x[4]:
                        case 'SCSS':
                            return 6
                        case 'TEX':
                            return 7
        case 1980:
            match x[1]:
                case 1960:
                    return 8
                case 1976:
                    return 13
                case 2009:
                    match x[2]:
                        case 'C++':
                            return 11
                        case 'SCAML':
                            return 12
                        case 'HAML':
                            match x[4]:
                                case 'SCSS':
                                    return 9
                                case 'TEX':
                                    return 10


print(func(['YANG', 2009, 'HAML', 2018, 'TEX']))
print(func(['LEAN', 1960, 'HAML', 2018, 'TEX']))
print(func(['LEAN', 2009, 'HAML', 1980, 'TEX']))
print(func(['YANG', 2009, 'HAML', 1980, 'SCSS']))
print(func(['LEAN', 1960, 'SCAML', 1980, 'SCSS']))
''''''
def func(x):
    a = bin(int(x, 10))[2:]
    a = '0' * (30 - len(a)) + a
    a = '0b' + a[0:3] + a[20:26] + a[10:19] + a[3:10] + a[26:30] + '0'
    return (str(hex(int(a, 2))))

print(func('573941375'))
print(func('573941375') == '0x24eb447e')
'''
import math

'''
def func(x):
    a = bin(int(x, 10))[2:]
    a = '0' * (30 - len(a)) + a
    a = '0b' + a[0:3] + a[20:26] + a[10:19] + a[3:10] + a[26:30] + '0'
    return (str(hex(int(a, 2))))

print(func('573941375'))
print(func('573941375') == '0x24eb447e')
'''
'''
class Programmer:
    def __init__(self, name, position):
        self.earned_money = 0
        self.name = name
        self.position = position
        self.worked = 0
        if self.position == "Junior":
            self.salary_per_hour = 10
        elif self.position == "Middle":
            self.salary_per_hour = 15
        else:
            self.salary_per_hour = 20

    def rise(self):
        if self.position == "Senior":
            self.salary_per_hour += 1
        elif self.position == "Junior":
            self.position = "Middle"
            self.salary_per_hour = 15
        else:
            self.position = "Senior"
            self.salary_per_hour = 20

    def work(self, time):
        self.worked += time
        self.earned_money += time * self.salary_per_hour

    def info(self):
        return f"{self.name} {self.worked}ч. {self.earned_money}тгр."



programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
'''

'''
class Rectangle:
    def __init__(self, point1, point2):
        self.x1 = point1[0]
        self.y1 = point1[1]
        self.x2 = point2[0]
        self.y2 = point2[1]
        if(self.x1 > self.x2):
            self.side1 = self.x1 - self.x2
        else:
            self.side1 = self.x2 - self.x1
        if (self.y1 > self.y2):
            self.side2 = self.y1 - self.y2
        else:
            self.side2 = self.y2 - self.y1


    def area(self):
        return round(self.side1*self.side2, 2)

    def get_pos(self):
        return round(self.x1, self.y1)

    def perimeter(self):
        return round(2 * (self.side1+self.side2), 2)

    def __repr__(self):
        return f'Rectangle({self.x1=}, {self.y1=}, {self.x2=}, {self.y2=})'


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
'''

'''
class Rectangle:
    def __init__(self, a, b):
        self.a = list(a)
        self.b = list(b)
        self.height = abs(a[0] - b[0])
        self.width = abs(a[1] - b[1])

    def perimeter(self):
        return round((self.height + self.width) * 2, 2)

    def area(self):
        return round(self.height * self.width, 2)

    def get_pos(self):
        return round(min(self.a[0], self.b[0]), 2), \
               round(max(self.a[1], self.b[1]), 2)

    def get_size(self):
        return round(self.height, 2), round(self.width, 2)

    def move(self, dx, dy):
        self.a[0] = self.a[0] + dx
        self.b[0] += dx
        self.a[1] += dy
        self.b[1] += dy
        self.height = abs(self.a[0] - self.b[0])
        self.width = abs(self.a[1] - self.b[1])

    def resize(self, width, height):
        self.a[0] = min(self.a[0], self.b[0])
        self.a[1] = max(self.a[1], self.b[1])
        self.b[0] = self.a[0] + width
        self.b[1] = self.a[1] - height
        self.height = abs(self.a[0] - self.b[0])
        self.width = abs(self.a[1] - self.b[1])

    def turn(self):
        mid_x = (self.a[0] + self.b[0]) / 2
        mid_y = (self.a[1] + self.b[1]) / 2
        self.a[0], self.a[1] = mid_x - (self.b[1] - mid_y), mid_y - (mid_x - self.a[0])
        self.b[0], self.b[1] = mid_x + (mid_y - self.a[1]), mid_y + (self.b[0] - mid_x)
        self.height = abs(self.a[0] - self.b[0])
        self.width = abs(self.a[1] - self.b[1])

    def scale(self, factor):
        mid_x = (self.a[0] + self.b[0]) / 2
        mid_y = (self.a[1] + self.b[1]) / 2
        self.a[0], self.a[1] = round(mid_x - (self.width * factor) / 2, 2), round(mid_y - (self.height * factor) / 2, 2)
        self.b[0], self.b[1] = round(mid_x + (self.width * factor) / 2, 2), round(mid_y + (self.height * factor) / 2, 2)
        self.height = abs(self.a[0] - self.b[0])
        self.width = abs(self.a[1] - self.b[1])

rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.turn()
print(rect.get_pos(), rect.get_size(), sep='\n')
'''
'''
import re


def main(x):
    r = r"\[\[\s*opt\s*list\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    z = re.findall(r, x)
    ls2 = []
    for ints, key in z:
        ls = []
        for i in ints.split():
            if i == ".":
                continue
            ls.append(int(i))
        p = (key, ls)
        ls2.append(p)
    return ls2

'''
'''
def main(a):
    b = []
    for i in range(len(a)):
        b.append([])
        k = 0
        for j in range(i+1, (len(a))):
            if a[i][3] == a[j][3]:
                k = 1
                break
        if k != 1:
            b[i].append(str(a[i][0]))
            if len(b[i][0]) < 5:
                b[i][0] = b[i][0] + (5 - len(b[i][0])) * "0"
            if a[i][1] == "true":
                b[i].append("да")
            else:
                b[i].append("нет")
            b[i].append(a[i][2][a[i][2].find(" ")+1:])
            b[i].append(a[i][4][a[i][4].find(")") + 1:])
            b[i][3] = b[i][3][:6] + b[i][3][7:]
    j = 0
    while j < len(b):
        if b[j] == []:
            del b[j]
        else:
            j += 1
    b.sort(key=lambda x: x[2])  # сортировка по третьему столбцу
    return (b)


с = [[0.26, "true", "П.С.Шацман", "П.С.Шацман", "7(869)352-59-94"],
     [0.26, "true", "П.С.Шацман", "П.С.Шацман", "7(869)352-59-94"],
     [0.26, "true", "П.С.Шацман", "П.С.Шацман", "7(869)352-59-94"],
     [0.83, "false", "Т.А.Бусяк", "Т.А.Бусяк", "+7(952)864-03-74"],
     [0.00, "true", "С.Ш.Шокянц", "С.Ш.Шокянц", "+7(508)426-73-76"],
     [0.69, "false", "Г.Ф.Гинасич", "Г.Ф.Гинасич", "+7(004)523-02-83"]]
d = [['0.57', 'true', 'Л.Е. Золберг', 'Л.Е. Золберг', '+7(082)081-95-95'],
     ['0.31', 'false', 'Е.Б. Шародич', 'Е.Б. Шародич', '+7(875)461-93-20'],
     ['0.03', 'false', 'Т.Д. Дебий', 'Т.Д. Дебий', '+7(693)575-07-62'],
     ['0.31', 'false', 'Е.Б. Шародич', 'Е.Б. Шародич', '+7(875)461-93-20'],
     ['0.31', 'false', 'Е.Б. Шародич', 'Е.Б. Шародич', '+7(875)461-93-20']]

print(main(с))
print(main(d))
'''

'''
1.1. (уровень сложности: низкий)

Напишите функцию deriv для приближенного вычисления производной в заданной точке.

Пример работы:

>>> deriv(lambda x: x ** 3)(5)
75.00014999664018
'''
def deriv(function, dx = 0.00001):
    return lambda x: (function(x + dx) - function(x)) / dx

print(deriv(lambda x: x**3)(5))

'''
1.3. (уровень сложности: низкий)

Реализуйте рекурсивное вычисление факториала в виде выражения. Необходимо 
это сделать без использования именованных функций, переменных (
в том числе без имени факториала) и присваиваний.
'''
print((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args))))(lambda f: lambda n: (1 if n == 0 else n * f(n-1)))(5))

'''
2.1 2.2 2.3
Создайте тип данных односвязный список с помощью ФВП. При создании списка нельзя использовать классы, готовые списки, кортежи и так далее.

Добавьте ряд операций в функциональном стиле.

2.1. (уровень сложности: высокий)

Создайте функцию pair(head, tail), которая порождает элемент списка. Не используйте ветвления. Создайте также функции head(lst) (возвращает значение головы списка) и tail(lst) (возвращает хвост списка).

2.2. (уровень сложности: средний)

Создайте функцию make_list(*args), которая создает список на основе аргументов.

2.3. (уровень сложности: средний)

Создайте функцию list_to_string(lst), возвращающую строку, содержащую элементы списка.
'''
#определяем функции для создания и работы со списком
def pair(head, tail):
    return lambda f: f(head, tail)

def head(lst):
    return lst(lambda head, tail: head)

def tail(lst):
    return lst(lambda head, tail: tail)

def make_list(*args):
    result = None
    for value in reversed(args):
        result = pair(value, result)
    return result

def list_to_string(lst):
    result = ""
    while lst != None:
        result += str(head(lst)) + ", "
        lst = tail(lst)
    return "[" + result[:-2] + "]"      # удаляем последнюю запятую и пробел, закрываем скобками

#создаем список
my_list = make_list(1, 2, 3, 4, 5)

#выводим значение головы списка
print(head(my_list))    # 1

#выводим хвост списка
print(list_to_string(tail(my_list)))   # [2, 3, 4, 5]

#выводим весь список в виде строки
print(list_to_string(my_list))   # [1, 2, 3, 4, 5]



