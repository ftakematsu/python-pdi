import cv2
import numpy as np

# Carregue a imagem
imagem = cv2.imread('sua_imagem.jpg')

# Verifique se a imagem foi carregada corretamente
if imagem is None:
    print('Não foi possível carregar a imagem.')
else:
    # Converta a imagem para o formato de cores RGB (padrão do OpenCV é BGR)
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # Armazene as informações de cores em uma matriz
    matriz_de_cores = np.array(imagem_rgb)

    # Agora você pode acessar as informações de cores da matriz
    # Por exemplo, para obter a cor do pixel na linha 10 e coluna 20:
    cor_do_pixel = matriz_de_cores[10, 20]

    print(f'Cor do pixel (linha 10, coluna 20): {cor_do_pixel}')



# Carregue a imagem
imagem = cv2.imread('sua_imagem.jpg')

# Verifique se a imagem foi carregada corretamente
if imagem is None:
    print('Não foi possível carregar a imagem.')
else:
    # Modifique os pixels da imagem
    for i in range(imagem.shape[0]):  # Percorra todas as linhas da imagem
        for j in range(imagem.shape[1]):  # Percorra todas as colunas da imagem
            # Altere a cor do pixel (i, j) para vermelho (255, 0, 0)
            imagem[i, j] = [255, 0, 0]

    # Salve a imagem modificada
    cv2.imwrite('imagem_modificada.jpg', imagem)

    print('Imagem modificada e salva com sucesso.')
