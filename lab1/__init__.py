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
'''
def func(x):
    a = bin(int(x, 10))[2:]
    a = '0' * (30 - len(a)) + a
    a = '0b' + a[0:3] + a[20:26] + a[10:19] + a[3:10] + a[26:30] + '0'
    return (str(hex(int(a, 2))))

print(func('573941375'))
print(func('573941375') == '0x24eb447e')
