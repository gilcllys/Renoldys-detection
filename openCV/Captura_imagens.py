import cv2
import numpy as np
import urllib.request
import os

URL = 'http://192.168.0.24/cam-hi.jpg'
Dados = 'com_chapeu'

if not os.path.exists(Dados):
	print('Pasta Criada: ', Dados)
	os.makedirs(Dados)

count = 0
cv2.namedWindow("ESP-32 CAM", cv2.WINDOW_AUTOSIZE)
while True:
    img_resp=urllib.request.urlopen(URL)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    im = cv2.imdecode(imgnp,-1)
    foto = im.copy()
    
    key=cv2.waitKey(5)
    if key == ord('s'):
        cv2.imwrite(Dados+'/objeto_{}.jpg'.format(count),foto)
        print('Imagem capturada: ', 'objeto_{}.jpg'.format(count))
        count = count + 1

    if key==ord('q'):
        break

    cv2.imshow('ESP-32 CAM',im)

cv2.destroyAllWindows()