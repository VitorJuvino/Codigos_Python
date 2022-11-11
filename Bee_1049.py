
# Bee1049

import os

os.system('cls')

def animal():

    tp1 = input()
    tp2 = input()
    tp3 = input()

    if tp1 == 'vertebrado':
        if tp2 == 'ave':
            if tp3 == 'carnivoro':
                print(f'aguia')
            elif tp3 == 'onivoro':
                print(f'pomba')
        elif tp2 == 'mamifero':
            if tp3 == 'onivoro':
                print(f'homem')
            elif tp3 == 'herbivoro':
                print(f'vaca')

    elif tp1 == 'invertebrado':
        if tp2 == 'inseto':
            if tp3 == 'hematofago':
                print(f'pulga')
            elif tp3 == 'herbivoro':
                print(f'lagarta')
        elif tp2 == 'anelideo':
            if tp3 == 'hematofago':
                print(f'sanguessuga')
            elif tp3 == 'onivoro':
                print(f'minhoca')

animal()
