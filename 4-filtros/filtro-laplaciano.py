# Importação da biblioteca de Imagem do Python
from PIL import Image

def aplicarMascara(lista, kernel):
    soma = 0
    for i in range(len(kernel)):
        soma += lista[i]*kernel[i]
    return soma


def filtroLaplaciano(imageFile, tipoMatriz, n=1):
    # Definindo a matriz de pesos
    if (tipoMatriz==1):
        kernel = [0, -1, 0, -1, 4, -1, 0, -1, 0]
    else:
        kernel = [-1, -1, -1, -1, 8, -1, -1, -1, -1]
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
            # Aplicar a matriz de pesos sobre os 9 pixels
            novoR = aplicarMascara(listaR, kernel)
            novoB = aplicarMascara(listaB, kernel)
            novoG = aplicarMascara(listaG, kernel)
            bitMapNew[i,j] = (novoR, novoB, novoG)
    return filtroLaplaciano(newImage, tipoMatriz, n-1)

originalImage = Image.open("_images/lenna.png")
originalImage.show()

# Aplicar o filtro da mediana
n = 1 # Representa o número de repetições da aplicação do filtro
tipoMatriz = 1
newImage = filtroLaplaciano(originalImage, tipoMatriz, n)

newImage.show()
