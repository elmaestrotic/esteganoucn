from PIL import Image

def is_bit_set(byte, bit):
    # Verifica si un bit específico está establecido en un byte
    return (byte & (1 << bit)) != 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Formato: Decode imagen")
        sys.exit(0)

    img_in = sys.argv[1]

    # Cargar imagen
    try:
        img = Image.open(img_in)
    except Exception as e:
        print(e)
        sys.exit(0)

    # Obtener mensaje
    message = ""
    for i in range(0, (img.width * img.height) - 3, 3):
        car = 0  # Inicializar como un número entero
        # Primer pixel
        ycoord = i // img.width
        xcoord = i - (ycoord * img.width)
        r, g, b = img.getpixel((xcoord, ycoord))

        # Si el bit menos significativo del color rojo está establecido, establece el bit 0 de 'car'
        if is_bit_set(r, 0):
            car |= 1 << 0
        # Si el bit menos significativo del color verde está establecido, establece el bit 1 de 'car'
        if is_bit_set(g, 0):
            car |= 1 << 1
        # Si el bit menos significativo del color azul está establecido, establece el bit 2 de 'car'
        if is_bit_set(b, 0):
            car |= 1 << 2

        # Segundo pixel
        ycoord = (i + 1) // img.width
        xcoord = i + 1 - (ycoord * img.width)
        r, g, b = img.getpixel((xcoord, ycoord))

        # Si el bit menos significativo del color rojo está establecido, establece el bit 3 de 'car'
        if is_bit_set(r, 0):
            car |= 1 << 3
        # Si el bit menos significativo del color verde está establecido, establece el bit 4 de 'car'
        if is_bit_set(g, 0):
            car |= 1 << 4
        # Si el bit menos significativo del color azul está establecido, establece el bit 5 de 'car'
        if is_bit_set(b, 0):
            car |= 1 << 5

        # Tercer pixel
        ycoord = (i + 2) // img.width
        xcoord = i + 2 - (ycoord * img.width)
        r, g, b = img.getpixel((xcoord, ycoord))

        # Si el bit menos significativo del color rojo está establecido, establece el bit 6 de 'car'
        if is_bit_set(r, 0):
            car |= 1 << 6
        # Si el bit menos significativo del color verde está establecido, establece el bit 7 de 'car'
        if is_bit_set(g, 0):
            car |= 1 << 7

        # Si el carácter construido es '#', se rompe el bucle
        if chr(car) == '#':
            break
        # Añade el carácter construido al mensaje
        message += chr(car)

    # Imprime el mensaje decodificado
    print(message)