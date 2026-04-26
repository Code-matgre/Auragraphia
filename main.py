import renders
import generator


def creazione():
    length = int(input("Quanto deve essere lunga?"))
    height = int(input("Quanto deve essere alta?"))
    scale = int(input("Quanto deve essere zoomata"))
    
    name = input("Come vuoi salvare la mappa?")
    time  = int(input("Quante vuoi crearne?"))

    startmatr = generator.initialize(length, height)
    
    for i in range(time):
        seed = generator.seed_generation()
        matr = generator.genera_mappa(startmatr, length, height, scale, seed)
        renders.disegna_mappa(matr, length, height, name, i)
    return 0

creazione()