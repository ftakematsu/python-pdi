# Importação da biblioteca de Imagem do Python
from PIL import Image
import math

def filtroMediana(imageFile, n=1):
    if (n==0):
        return imageFile
    # Extrair o tamanho da imagem (em pixels)
    altura,largura = imageFile.width, imageFile.height
    newImage = Image.new(mode="RGB", size=(altura, largura))
    # Extrair a matriz de pixels da imagem
    bitMapNew = newImage.load()
    # Percorre a imagem sem considerar as bordas (extremidades)
    for i in range(1, altura-1):
        for j in range(1, largura-1):
            x = i-1
            # Inicializa as listas para armazenar os valores dos 9 pixels 
            listaR = []
            listaG = []
            listaB = []
            while x<=i+1:
                y = j-1
                while y<=j+1:
                    r, g, b = imageFile.getpixel((x,y))
                    # Inclui os valores de r,g,b nas listas
                    listaR.append(r)
                    listaG.append(g)
                    listaB.append(b)
                    y+=1
                x+=1
            # Ordenar as listas (em ordem crescente)
            listaR.sort()
            listaG.sort()
            listaB.sort()
            # Após a ordenação, obter o valor da mediana de cada lista
            # Como cada lista tem 9 elementos, a mediana (posição central) será sempre a posição 4
            bitMapNew[i,j] = (listaR[4], listaG[4], listaB[4])
    return filtroMediana(newImage, n-1)

#originalImage = Image.open("_images/lenna.png")
originalImage = Image.open("_images/lenna-ruidos.png")
originalImage.show()

# Aplicar o filtro da mediana
n = 2 # Representa o número de repetições da aplicação do filtro
newImage = filtroMediana(originalImage, n)

newImage.show()
