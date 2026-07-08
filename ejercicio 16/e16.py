from PIL import Image
import matplotlib.pyplot as plt

imagen = Image.open("scooby_doo.jpg").convert("RGB")

def escala_grises(img):
    ancho, alto = img.size
    nueva = Image.new("L", (ancho, alto))

    for i in range(ancho):
        for j in range(alto):
            R, G, B = img.getpixel((i, j))

            gris = int(R * 0.2989 + G * 0.5870 + B * 0.1140)

            nueva.putpixel((i, j), gris)

    return nueva

imagen_gris = escala_grises(imagen)

plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.imshow(imagen)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(imagen_gris, cmap="gray")
plt.title("Escala de Grises")
plt.axis("off")

plt.show()