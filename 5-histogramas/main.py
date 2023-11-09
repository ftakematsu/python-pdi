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


# Converter a imagem em escala de cinza
def converterParaEscalaCinza(imageFile):
    bitMap = imageFile.load()
    altura,largura = imageFile.width, imageFile.height
    for i in range(altura):
        for j in range(largura):
            r,g,b,a = imageFile.getpixel((i,j))
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
            r,g,b,a = imageFile.getpixel((i,j))
            # Extraindo o tom de cinza da imagem
            cinza = tomCinza(r,g,b)
            histograma.definirFrequencia(cinza)
    histograma.imprimirTabela()
    return imageFile

imageFile = Image.open("_images/lenna-contraste-baixo.png")
imageFile = calcularHistograma(imageFile)


#imageFile.save("_outputs/new_image.png", format="png")
imageFile.show()

# Mostra o gráfico via Matplotlib
histograma.mostrarGrafico()