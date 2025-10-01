# -*- coding: utf-8 -*-
"""

@author: Nazar Yemelianov
"""

def dec_to_bin(x):
    '''
    Przetwarza liczby z dziesiętnej systemy w dwójkową systemę liczb
    Args:
        x(int): liczba do przetwarzenia
    Returns:
        binar(str): przetwarzona liczba w dwójkowej systemie
    '''
    binar = str()
    if x<=0:
        return "-"
    while x!=0:
        x = x//2
        if x%2==0:
             binar += "0"
        else:
            binar += "1"
    return binar
x = input("Podaj liczbę dla binara: ")
try:
    print(dec_to_bin(int(x)))
except ValueError:
    print("Podaj liczbę!")
