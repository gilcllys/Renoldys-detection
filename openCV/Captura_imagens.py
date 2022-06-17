import cv2
import numpy as np
import urllib.request
import os

# url utilizada para fazer a conexão com o módulo ESP-32 conectado na rede wiffi
URL = 'http://192.168.0.24/cam-hi.jpg'

#Nome da pasta criada para armazenar os dados que serão utilizados futuramente para o treinamento da IA
# 'com_chapeu' é um nome que pode ser trocado de acordo com a necessidade da pessoa
Dados = 'sem_chapeu'
nome_arquivos = 'S_Chapeu'
# Lógica para verificar se ja existe algum diretório com o nome
if not os.path.exists(Dados):
	print('Pasta Criada: ', Dados)
	os.makedirs(Dados)

# Contador para identificar a ordem das fotos capturadas
count = 0
#Nome que ficara na janela criada ao executar o algoritmo
cv2.namedWindow("ESP-32 CAM", cv2.WINDOW_AUTOSIZE)

#Loop principal responsável por processar cada imagem gerada pelo módulo ESP-32
while True:
    # Consumindo e tratando as imagens fornecidas do módulo ESP-32
    img_resp=urllib.request.urlopen(URL)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    im = cv2.imdecode(imgnp,-1)

    # Fazendo uma cópia do frame e guardando na variável foto
    foto = im.copy()
    # Identificar uma tecla pressionada no teclado
    key=cv2.waitKey(5)
    # Caso a tecla s seja pressionada, o frame armazenado na variável foto será salvo no diretório com o nome criado anteriomente criado na Dados e salvo no formato .jpg
    if key == ord('s'):
        cv2.imwrite(Dados+'/{}_{}.jpg'.format(nome_arquivos,count),foto)
        print('Imagem capturada: ', '{}_{}.jpg'.format(nome_arquivos,count))
        count = count + 1

    # Pressionando a tecla q você encerra o programa por completo
    if key==ord('q'):   
        # comando fecha e encerra todas as janelas abertas
        cv2.destroyAllWindows()
        break
    # comando responsável por exibir as imagens em tempo real
    cv2.imshow('ESP-32 CAM',im)
