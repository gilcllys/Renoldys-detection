import numpy as np 
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model


width = 640
height = 480

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4, height)
margem = 0.7
novo_modelo = load_model('./m_treinado.h5')

def preProcessamento(img):
    #colocando em escala cinza
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # equalizando as imagens
    img = cv2.equalizeHist(img)
    # normalizando as imagens
    img = img /255
    return img

while True:
    success, imagemOriginal  = cap.read()
    img = np.asanyarray(imagemOriginal)
    img = cv2.resize(img,(32,32))
    img = preProcessamento(img)
    #cv2.imshow('Imagem Processada',img)
    img = img.reshape(1,32,32,1)
    # predições
    classIndex = novo_modelo.predict(img)
    
    def getCalssName(classNo):
        if   classNo == 0: return 'Sem chapeu'
        elif classNo == 1: return 'Com chapeu'
        
    probabilidade = np.amax(classIndex)
    classIndex = np.argmax(classIndex[0])
    label = getCalssName(classIndex)
    print(classIndex,probabilidade)

    if probabilidade > margem:
       cv2.putText(imagemOriginal,str(label) +'  '+str(probabilidade),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1) 
    cv2.imshow('Imagem orginal',imagemOriginal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break