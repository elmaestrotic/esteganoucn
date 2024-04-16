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
    chars = message.encode("ASCII")#codifica en ASCII. El resultado es una secuencia de bytes, donde cada byte representa un carácter del mensaje en ASCII
    for char in chars:#itera sobre cada byte en `chars` que representa un carácter en ASCII
        for j in range(3):#permite iterar sobre los primeros 3 bits en el byte char.
            ycoord = pix_index // img.width #obtenemos la coordenada y
            xcoord = pix_index - (ycoord * img.width) #obtenemos la coordenada x
            r, g, b = img.getpixel((xcoord, ycoord))#obtenemos los valores de RGB del pixel actual
           #ahora vamos a modificar el valor de RGB, empezamos con el rojo r
            if is_bit_set(char, (j * 3) + 0):#invocamos esta función para verificar si el bit en las posición `(j * 3) + 0 está establecido (es decir, si es 1)
                r |= 1 << 0#establece el bit menos significativo de `r` en 1
            else:
                r &= ~(1 << 0)#establece el bit menos significativo de `r` en 0

            if is_bit_set(char, (j * 3) + 1):#invocamos esta función para verificar si el bit en las posición `(j * 3) +  1 está establecido
                g |= 1 << 0
            else:
                g &= ~(1 << 0)

            if j < 2:  # No usamos el último byte
                if is_bit_set(char, (j * 3) + 2):#invocamos esta función para verificar si el bit en las posición [2] está establecido
                    b |= 1 << 0
                else:
                    b &= ~(1 << 0)

            img.putpixel((xcoord, ycoord), (r, g, b))# a medida que vamos modificando los valores de RGB, los vamos guardando en la imagen
            pix_index += 1

    # Guardar imagen
    try:
        img.save("codificada.png")
    except Exception as e:
        print(e)
