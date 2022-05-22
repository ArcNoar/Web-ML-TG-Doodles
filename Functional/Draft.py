from random import randint
import numpy as np


# G3/4 Pm 1/4 L3

Dima = ((((0.75 * (0.75 / (2/4)))) + ((0.75 * (0.25 / (2/4))))) + (((0.25 / (0.75 / (2/4)))) + ((0.25 * (0.25 / (2/4)))))) * 10



Masha = ((((0.5 * (0.75 / (3/4)))) + ((0.5 * (0.25 / (3/4))))) + (((0.5 / (0.5 / (3/4)))) + ((0.5 * (0.75 / (3/4)))))) * 10

D_battle_point = round((Dima * 10),2)

M_battle_point = round((Masha * 10),2)

print(f'Dima Score : {D_battle_point}')

print(f'Masha Score : {M_battle_point}')