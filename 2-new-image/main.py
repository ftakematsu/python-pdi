import math
from PIL import Image
import random

# Dimensões da imagem
largura = 300
altura = 300

# Cria uma nova imagem
imageFile = Image.new(mode="RGB", size=(largura, altura))

# Extrair a matriz de pixels da imagem
bitMap = imageFile.load()

# Extrai informações de pixel da imagem (formato RGB)
for i in range(altura):
    for j in range(largura):
        r = math.floor(random.random()*255)
        g = math.floor(random.random()*255)
        b = math.floor(random.random()*255)
        bitMap[i,j] = (r,g,b)

imageFile.save("_outputs/image2.png", format="png")
imageFile.show()
