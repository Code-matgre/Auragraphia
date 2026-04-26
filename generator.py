
from noise import snoise2
import random
import os


os.makedirs("output", exist_ok=True)

def initialize(length, height):
    matr = []
    for i in range(height):
        row = []
        for j in range(length):
            row.append(0)
        matr.append(row)
    return matr
 



def seed_generation(): 
    seed = random.randint(0, 999999)
    return seed

def genera_mappa(matr, length, height, scale, seed):
    
    for i in range(height):
        for j in range(length):
            valore = snoise2(i/scale, j/scale, octaves=6, base=seed)
            matr[i][j] = (valore+1)/2
    return matr


