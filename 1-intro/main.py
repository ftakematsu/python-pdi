# Importação da biblioteca de Imagem do Python
from PIL import Image
import math

imageFile = Image.open("_images/lenna.png")

# Extrair a matriz de pixels da imagem
bitMap = imageFile.load()

# Extrair o tamanho da imagem (em pixels)
altura,largura = imageFile.width, imageFile.height
print(f"Altura da imagem: {altura}")
print(f"Largura da imagem: {largura}")

def escalaCinza(r, g, b):
    cinza = math.floor((r+g+b)/3)
    return (cinza, cinza, cinza)

def inverteImagem(r, g, b):
    return (255-r, 255-g, 255-b)

def pretoBranco(r, g, b, limiar):
    cinza = math.floor((r+g+b)/3)
    if (cinza>=limiar):
        tomCor = 255
    else: 
        tomCor = 0
    return (tomCor, tomCor, tomCor)

# Extrai informações de pixel da imagem (formato RGB)
for i in range(altura):
    for j in range(largura):
        # Obtêm os valores de RGB na posição i,j
        r,g,b = imageFile.getpixel((i,j))
        #print(f"({r},{g},{b})", end="")
        # Atribuir uma cor para a posição do pixel
        # bitMap[i,j] = escalaCinza(r,g,b)
        # bitMap[i,j] = inverteImagem(r,g,b)
        bitMap[i,j] = pretoBranco(r,g,b, 120)
    #print()

imageFile.save("_outputs/new_image.png", format="png")
imageFile.show()