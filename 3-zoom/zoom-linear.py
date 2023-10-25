# Importação da biblioteca de Imagem do Python
from PIL import Image
import math

def media(p1, p2):
    return math.floor((p1+p2)/2)

def zoomLinear(imageFile):
    # Extrair o tamanho da imagem (em pixels)
    altura,largura = imageFile.width, imageFile.height
    print(f"Altura da imagem: {altura}")
    print(f"Largura da imagem: {largura}")
    newImage = Image.new(mode="RGB", size=(altura*2, largura*2))
    # Extrair a matriz de pixels da imagem
    bitMapNew = newImage.load()
    i = 0
    x = 0
    # Processo de definir pixels vazios entre os pontos
    while i<altura:
        j = 0
        y = 0
        while j<largura-1:
            # Obtém o valor do pixel atual
            r,g,b = imageFile.getpixel((i,j))
            bitMapNew[x, y] = (r,g,b)
            j+=1
            y+=2
        i+=1
        x+=2
    # Calcular a média sobre as linhas da matriz
    i=0
    while i<newImage.height:
        j=1
        while j<newImage.width-1:
            r1,g1,b1 = newImage.getpixel((i,j-1))
            r2,g2,b2 = newImage.getpixel((i,j+1))
            bitMapNew[i, j] = (media(r1,r2), media(g1,g2), media(b1,b2))
            j+=2
        i+=2
    # Calcular a média sobre as colunas da matriz
    i=1
    while i<newImage.height-1:
        j=0
        while j<newImage.width:
            r1,g1,b1 = newImage.getpixel((i-1,j))
            r2,g2,b2 = newImage.getpixel((i+1,j))
            bitMapNew[i, j] = (media(r1,r2), media(g1,g2), media(b1,b2))
            j+=1
        i+=2
    return newImage


originalImage = Image.open("_images/lenna.png")
originalImage.show()

# Aplicando zoom
newImage = zoomLinear(originalImage)

newImage.show()
