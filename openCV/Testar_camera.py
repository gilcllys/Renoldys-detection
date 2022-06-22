import cv2
import numpy as np
import urllib.request
import os

# url utilizada para fazer a conexão com o módulo ESP-32 conectado na rede wiffi
URL = 'http://192.168.0.24/cam-hi.jpg'

#Nome que ficara na janela criada ao executar o algoritmo
cv2.namedWindow("ESP-32 CAM", cv2.WINDOW_AUTOSIZE)

#Loop principal responsável por processar cada imagem gerada pelo módulo ESP-32
while True:
    # Consumindo e tratando as imagens fornecidas do módulo ESP-32
    img_resp=urllib.request.urlopen(URL)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    im = cv2.imdecode(imgnp,-1)

    # Identificar uma tecla pressionada no teclado
    key=cv2.waitKey(5)
    # Pressionando a tecla q você encerra o programa por completo
    if key==ord('q'):   
        # comando fecha e encerra todas as janelas abertas
        cv2.destroyAllWindows()
        break
    # comando responsável por exibir as imagens em tempo real
    cv2.imshow('ESP-32 CAM',im)
