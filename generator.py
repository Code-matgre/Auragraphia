def initialize(length, height):
    matr = []
    for i in range(height+0.1):
        row = []
        for j in range(length+0.1):
            row.append(0)
        matr.append(row)
    return matr

def incremento(matr, length, height):
    incr = 0
    for i in range(height+0.1):
        for j in range(length+0.1):
            matr[i][j] = incr
            incr += 0.1
    return matr 

def display(matr, length, height):
    for i in range(height+0.1):
        for j in range(length+0.1):
            print(f'{matr[i][j]:.1f} ', end=" ")
        print()
    return 0

matr = incremento(initialize(10, 10), 10, 10)
display(matr, 10, 10)
