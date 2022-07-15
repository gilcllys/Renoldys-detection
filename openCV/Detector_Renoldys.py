import numpy as np 
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import urllib.request

width = 640
height = 480

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4, height)
margem = 0.7
novo_modelo = load_model('./m_treinado.h5')

def preProcessamento(img):
    img =cv2.resize(img,(32,32))
    #colocando em escala cinza
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # equalizando as imagens
    img = cv2.equalizeHist(img)
    # normalizando as imagens
    img = img /255
    return img

# url utilizada para fazer a conexão com o módulo ESP-32 conectado na rede wiffi
#URL = 'http://192.168.0.24/cam-hi.jpg'
URL = 'http://192.168.239.203:8080/shot.jpg'
    

while True:
    # Consumindo e tratando as imagens fornecidas do módulo ESP-32
    img_resp= urllib.request.urlopen(URL)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    imagemOriginal = cv2.imdecode(imgnp,-1)
    imagemPrcessada = preProcessamento(imagemOriginal)
    imagemPrcessada = imagemPrcessada.reshape(1,32,32,1)
    # predições
    classIndex = novo_modelo.predict(imagemPrcessada)
    
    def getCalssName(classNo):
        if   classNo == 0: return 'Laminar'
        elif classNo == 1: return 'Transição'
        elif classNo == 2 or classNo == 3: return 'Turbulante'
        
    probabilidade = np.amax(classIndex)
    classIndex = np.argmax(classIndex[0])
    label = getCalssName(classIndex)
    print(classIndex,probabilidade)

    if probabilidade > margem:
       cv2.putText(imagemOriginal,str(label) +'  '+str(probabilidade),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1) 
    cv2.imshow('Imagem orginal',imagemOriginal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break