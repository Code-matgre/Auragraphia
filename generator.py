from noise import snoise2
import random
import string
import os
from PIL import Image

os.makedirs("output", exist_ok=True)

def initialize(length, height):
    matr = []
    for i in range(height):
        row = []
        for j in range(length):
            row.append(0)
        matr.append(row)
    return matr
 
def disegna_mappa(matr, length, height, name, num):
    colors = {
        "oceano": (20, 60, 150),
        "sabbia": (210, 180, 140),
        "foresta": (34, 139, 34),
        "montagna": (100, 100, 100)
    }
    foto = Image.new("RGB", (length, height))

    for i in range(height):
        for j in range(length):
            if matr[i][j] < 0.3:
                foto.putpixel((j, i), colors["oceano"])
            elif matr[i][j] < 0.5:
                foto.putpixel((j, i), colors["sabbia"])
            elif matr[i][j] < 0.8:
                foto.putpixel((j, i), colors["foresta"])
            else:
                foto.putpixel((j, i), colors["montagna"])
    foto.save(f'output/{name}{num}.png')


def seed_generation(): 
    seed = random.randint(0, 999999)
    return seed

def genera_mappa(matr, length, height, scale, seed):
    
    for i in range(height):
        for j in range(length):
            valore = snoise2(i/scale, j/scale, octaves=6, base=seed)
            matr[i][j] = (valore+1)/2
    return matr
def creazione():
    length = int(input("Quanto deve essere lunga?"))
    height = int(input("Quanto deve essere alta?"))
    scale = int(input("Quanto deve essere zoomata"))
    
    name = input("Come vuoi salvare la mappa?")
    time  = int(input("Quante vuoi crearne?"))
    for i in range(time):
        seed = seed_generation()
        matr = genera_mappa(initialize(length, height), length, height, scale, seed)
        disegna_mappa(matr, length, height, name, i)
    return 0


length = 10
height = 10
scale = 10
seed = seed_generation()

creazione()

