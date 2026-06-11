def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""

    for letra in mensaje:
        if letra.isalpha():  

            if letra.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')

            nueva_letra = chr((ord(letra) - inicio + desplazamiento) % 26 + inicio)
            resultado += nueva_letra

        else:
            resultado += letra

    return resultado


mensaje = input("Ingrese un mensaje: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))

print("Resultado:", cifrado_cesar(mensaje, desplazamiento))