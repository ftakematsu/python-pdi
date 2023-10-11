# Importação da biblioteca de Imagem do Python
from PIL import Image

imageFile = Image.open("_images/rgb.png")

# Extrair a matriz de pixels da imagem
bitMap = imageFile.load()

# Extrair o tamanho da imagem (em pixels)
altura,largura = imageFile.width, imageFile.height
print(f"Altura da imagem: {altura}")
print(f"Largura da imagem: {largura}")

# Extrai informações de pixel da imagem (formato RGB)
for i in range(altura):
    for j in range(largura):
        # Obtêm os valores de RGB na posição i,j
        r,g,b = imageFile.getpixel((i,j))
        print(f"({r},{g},{b})", end="")
    print()
