from noise import snoise2
def initialize(length, height):
    matr = []
    for i in range(height):
        row = []
        for j in range(length):
            row.append(0)
        matr.append(row)
    return matr

def incremento(matr, length, height):
    incr = 0
    for i in range(height):
        for j in range(length):
            matr[i][j] = incr
            incr += 0.1
    return matr 

def display(matr, length, height):
    for i in range(height):
        for j in range(length):
            print(f'{matr[i][j]:.1f} ', end=" ")
        print()
    return 0
def new_display(matr, length, height):
    for i in range(height):
        for j in range(length):
            if matr[i][j] < 0.3:
                print(f'~', end=" ")
            elif matr[i][j] < 0.5:
                print(f'.', end=" ")
            elif matr[i][j] < 0.8:
                print(f'*', end=" ")
            else:
                print(f'^', end=" ")
        print()
    return 0   

def genera_mappa(matr, length, height, scale):
    
    for i in range(height):
        for j in range(length):
            valore = snoise2(i/scale, j/scale, octaves=6)
            matr[i][j] = (valore+1)/2
    return matr

length = 10
height = 10
scale = 10
matr = genera_mappa(initialize(length, height), length, height, scale)
new_display(matr, length, height)