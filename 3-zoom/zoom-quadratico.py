# Importação da biblioteca de Imagem do Python
from PIL import Image
import math

def zoomQuadratico(imageFile):
    # Extrair o tamanho da imagem (em pixels)
    altura,largura = imageFile.width, imageFile.height
    print(f"Altura da imagem: {altura}")
    print(f"Largura da imagem: {largura}")

    newImage = Image.new(mode="RGB", size=(altura*2, largura*2))

    # Extrair a matriz de pixels da imagem
    bitMapNew = newImage.load()

    i = 0
    x = 0
    while i<altura:
        j = 0
        y = 0
        while j<largura:
            # Obtêm os valores de RGB na posição i,j da imagem original
            r,g,b = imageFile.getpixel((i,j))
            bitMapNew[x, y] = (r,g,b)
            # Pixels vizinhos
            bitMapNew[x+1, y] = (r,g,b)
            bitMapNew[x, y+1] = (r,g,b)
            bitMapNew[x+1, y+1] = (r,g,b)
            j+=1
            y+=2
        i+=1
        x+=2
    return newImage


originalImage = Image.open("_images/lenna.png")

originalImage.show()

# Aplicando zoom
newImage = zoomQuadratico(originalImage)
newImage = zoomQuadratico(newImage)


newImage.show()
