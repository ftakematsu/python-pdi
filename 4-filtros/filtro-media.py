# Importação da biblioteca de Imagem do Python
from PIL import Image
import math

def filtroMedia(imageFile, n=1):
    if (n==0):
        return imageFile
    # Extrair o tamanho da imagem (em pixels)
    altura,largura = imageFile.width, imageFile.height
    print(f"Altura da imagem: {altura}")
    print(f"Largura da imagem: {largura}")
    newImage = Image.new(mode="RGB", size=(altura, largura))
    # Extrair a matriz de pixels da imagem
    bitMapNew = newImage.load()
    for i in range(altura):
        for j in range(largura):
            x = i-1
            cont = 0
            somaR = somaG = somaB = 0
            while x<=i+1:
                y = j-1
                while y<=j+1:
                    # Verifica se a posição está dentro da imagem
                    if ((x>=0 and x<altura) and (y>=0 and y<largura)):
                        r, g, b = imageFile.getpixel((x,y))
                        somaR+=r
                        somaG+=g
                        somaB+=b
                        cont+=1
                    y+=1
                x+=1
            # Após o cálcula da soma dos 9 pixels, calcular a média e atribuir para a nova imagem
            bitMapNew[i,j] = (math.floor(somaR/cont), math.floor(somaG/cont), math.floor(somaB/cont))
    return filtroMedia(newImage, n-1)


originalImage = Image.open("_images/lenna-ruidos.png")
originalImage.show()

# Aplicar o filtro da média
n = 4 # Representa o número de repetições da aplicação do filtro
newImage = filtroMedia(originalImage, n)

newImage.show()
