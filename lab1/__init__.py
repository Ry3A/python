import math

def func(x):
    return math.sqrt((55*(69 * x**3 + 2 * x**2 + 1)**4 - 7)
                     //(15*(2 * x + 73 + 75 * x**2) +
                        52*(1 - 42 * x**3 - 62 * x)**2)) + \
                        59*(54 * x - 29)**5

print(func(-0.69))