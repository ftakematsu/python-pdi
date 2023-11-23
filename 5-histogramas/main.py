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

def equalizarHistograma(imageFile):
    bitMap = imageFile.load()
    altura,largura = imageFile.width, imageFile.height
    for y in range(altura):
        for x in range(largura):
            r,g,b = getRGB(imageFile, y, x)
            rk = tomCinza(r,g,b)
            S = 0
            # Calcula o somatorio de probabilidade (acumulada) de 0 até rk
            for i in range(rk):
                S += histograma.frequencia[i]/histograma.pixels
            # Define o novo tom de cinza do pixel
            cinza = math.floor(S*255)
            bitMap[y,x] = (cinza,cinza,cinza)
    return imageFile

imageFile = Image.open("_images/wilderness.png")
imageFile = calcularHistograma(imageFile)
imageFile = equalizarHistograma(imageFile)
# Exibe o histograma após a equalização
imageFile = calcularHistograma(imageFile)

imageFile.show()

# Mostra o gráfico via Matplotlib
histograma.mostrarGrafico()