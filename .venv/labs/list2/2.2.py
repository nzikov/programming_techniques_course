# -*- coding: utf-8 -*-
"""

@author: Nazar Yemelianov
"""
import matplotlib.pyplot as plt
from numpy import random


def spacer(n):
    '''
    Symulacja spaceru osoby w losowych kierunkach
    Args:
        n(int): odległość spacera od punktu zero
    Returns:
        xy(list): punkty przemieszczenia spacerującego
    '''
    x1 = 0
    y1 = 0
    xy = [(x1, y1)]

    while n >= (x1 ** 2 + y1 ** 2) ** 0.5:

        kier = random.randint(4)
        if kier == 1:  # prawo
            x1 += 1
        if kier == 2:  # lewo
            x1 = x1 - 1
        if kier == 3:  # gora
            y1 += 1
        if kier == 4:  # dol
            y1 = y1 - 1
        xy.append((x1, y1))
    return xy


n = int(input("Jak daleko X ma odejść? \n"))
try:
    wsp = spacer(n)
except TypeError:
    print("Proszę podać arabskimi dodatnimi liczbami")
x, y = zip(*wsp)
plt.plot(x, y, marker='o', linestyle='-', markersize=2)
plt.xlabel('Współrzędna X')
plt.ylabel('Współrzędna Y')
plt.title('Trajektoria spacerowicza')
plt.grid(True)
plt.show()