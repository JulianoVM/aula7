import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('imagem3.jpg')
# imagem2 = cv2.imread('imagem2.jpg')

# Definir os pontos de origem e destino
pts_origem = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts_destino = np.float32([[10, 100], [200, 50], [100, 250], [250, 200]])

# Calcular a matriz de transformação perspectiva
matriz_perspectiva = cv2.getPerspectiveTransform(pts_origem, pts_destino)

# Aplicar a transformação
imagem_corrigida = cv2.warpPerspective(imagem, matriz_perspectiva, (imagem.shape[0], imagem.shape[1]))
# imagem_corrigida2 = cv2.warpPerspective(imagem2, matriz_perspectiva, (imagem2.shape[0], imagem2.shape[1]))

# Exibir resultado
cv2.imshow('Correção de Perspectiva', imagem_corrigida)
cv2.waitKey(0)

pts_origem = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts_destino = np.float32([[100, 50], [185, 50], [20, 200], [200, 200]])

matriz_perspectiva = cv2.getPerspectiveTransform(pts_origem, pts_destino)

imagem_corrigida = cv2.warpPerspective(imagem, matriz_perspectiva, (imagem.shape[1], imagem.shape[0]))

cv2.imshow('Correção de Perspectiva', imagem_corrigida)
cv2.waitKey(0)

cv2.destroyAllWindows()
