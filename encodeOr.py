from PIL import Image
import sys


def is_bit_set(byte, bit):
    return (byte & (1 << bit)) != 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Formato: Encode imagen \"texto\"")
        sys.exit(0)

    img_in = sys.argv[1]
    message = sys.argv[2]

    message = message + "#"

    # Cargar imagen
    try:
        img = Image.open(img_in)
    except Exception as e:
        print(e)
        sys.exit(0)

    if len(message) > ((img.width * img.height) // 3):
        print("El mensaje es demasiado grande para la imagen.")
        sys.exit(0)

    # Almacenar mensaje
    pix_index = 0
    chars = message.encode("ASCII")

    # Crear una imagen con los píxeles modificados resaltados en amarillo
    yellow_img = img.copy()
    yellow_pixels = yellow_img.load()

    # Lista para almacenar las coordenadas de los píxeles modificados
    modified_pixels = []

    for char in chars:
        for j in range(3):
            ycoord = pix_index // img.width
            xcoord = pix_index - (ycoord * img.width)
            r, g, b = img.getpixel((xcoord, ycoord))

            if is_bit_set(char, (j * 3) + 0):
                r |= 1 << 0
            else:
                r &= ~(1 << 0)

            if is_bit_set(char, (j * 3) + 1):
                g |= 1 << 0
            else:
                g &= ~(1 << 0)

            if j < 2:
                if is_bit_set(char, (j * 3) + 2):
                    b |= 1 << 0
                else:
                    b &= ~(1 << 0)

            img.putpixel((xcoord, ycoord), (r, g, b))
            if (r, g, b) != yellow_img.getpixel((xcoord, ycoord)):  # Si el píxel ha cambiado, marcarlo en amarillo
                yellow_pixels[xcoord, ycoord] = (255, 255, 0)  # Amarillo
                # Almacenar las coordenadas del píxel modificado en la lista
                modified_pixels.append((xcoord, ycoord))

            pix_index += 1

    # Guardar imágenes
    try:
        img.save("codificada.png")
        yellow_img.save("codificada2.png")
    except Exception as e:
        print(e)

    # Imprimir las coordenadas de los píxeles modificados y el total de píxeles modificados
    print("Coordenadas de los píxeles modificados:")
    #for coord in modified_pixels:
        #print(coord)
    print(modified_pixels)
    print("Total de píxeles modificados:", len(modified_pixels))
