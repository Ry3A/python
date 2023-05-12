
import math
import tkinter as tk
import random
import matplotlib.pyplot as plt
from random import randint


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    b = 0.2
    a = random.randint(0, 1)
    if(x < b and y < b) or (x > 1 - b and y < b):
        return 0, 0, 0
    b += 0.2
    if (x < b and y < b) or (x > 1 - b and y < b):
        return 255, 255, 255


    return x, y, 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()

'''
import matplotlib.pyplot as plt
from random import randint


def gen():
    orig = [[randint(0, 1) for j in range(10)] for i in range(5)]
    fig, ax = plt.subplots()
    ax.imshow(orig + orig[::-1])
    plt.show()


def genFor(x):
    for i in range(x):
        gen()


genFor(1)
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import itertools

table = np.random.uniform(low=0.0, high=1.0, size=(5,5))


plt.figure()
plt.imshow(table, interpolation='nearest', cmap=plt.cm.Greys, vmin=0, vmax=1)
plt.yticks(np.arange(4))

for i,j in itertools.product(range(table.shape[0]), range(table.shape[1])):
    plt.text(j, i, format(table[i,j], '.2f'),
             horizontalalignment="center",
             color="white" if table[i,j] > 0.5 else "black")

plt.show()
'''