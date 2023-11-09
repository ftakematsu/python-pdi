# Importação da biblioteca de Imagem do Python
from PIL import Image
import math
from histograma import Histograma

histograma = Histograma()

def escalaCinza(r, g, b):
    cinza = math.floor((r+g+b)/3)
    return (cinza, cinza, cinza)

def tomCinza(r, g, b):
    cinza = math.floor((r+g+b)/3)
    return cinza

def getRGB(imageFile, i, j):
    if (len(imageFile.getpixel((i,j)))==4):
        r,g,b,a = imageFile.getpixel((i,j))
    else:
        r,g,b = imageFile.getpixel((i,j))
    return (r,g,b)

# Converter a imagem em escala de cinza
def converterParaEscalaCinza(imageFile):
    bitMap = imageFile.load()
    altura,largura = imageFile.width, imageFile.height
    for i in range(altura):
        for j in range(largura):
            r,g,b = getRGB(imageFile, i, j)
            bitMap[i,j] = escalaCinza(r,g,b)
    return imageFile

# Histograma de uma imagem
# Extrair a distribuição de frequência dos tons de cinza da imagem
def calcularHistograma(imageFile):
    # Converte para escala de cinza
    imageFile = converterParaEscalaCinza(imageFile)
    # Extrair a altura e a largura da imagem
    altura,largura = imageFile.width, imageFile.height
    histograma.definirTotalPixels(altura*largura)
    for i in range(altura):
        for j in range(largura):
            r,g,b = getRGB(imageFile, i, j)
            # Extraindo o tom de cinza da imagem
            cinza = tomCinza(r,g,b)
            histograma.definirFrequencia(cinza)
    histograma.imprimirTabela()
    return imageFile

imageFile = Image.open("_images/lenna.png")
imageFile = calcularHistograma(imageFile)


imageFile.show()

# Mostra o gráfico via Matplotlib
histograma.mostrarGrafico()