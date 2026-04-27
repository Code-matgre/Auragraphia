from PIL import Image

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
            elif matr[i][j] < 0.7:
                foto.putpixel((j, i), colors["foresta"])
            else:
                foto.putpixel((j, i), colors["montagna"])
    foto.save(f'output/{name}{num}.png')