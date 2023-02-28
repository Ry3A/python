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
'''
import math

def func(n):
    if n == 0:
        return 0.44
    else:
        return func(n - 1) - (abs(func(n - 1)))**3 / 57

print(func(4))