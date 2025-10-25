import cv2
import easyocr
import matplotlib.pyplot as plt


imagen = "placa.jpg"

imagen = cv2.imread(imagen)
img_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

lector = easyocr.Reader(['es'], gpu=False)

resultado = lector.readtext(img_rgb)

#print(resultado)

#for _, texto, _ in resultado:
#    print(texto)



for (caja, texto, probabilidad) in resultado:
    print(probabilidad)
    
    (arriba_izq, arriba_der, abajo_der, abajo_izq) = caja
    arriba_izq = tuple(map(int, arriba_izq))
    arriba_der = tuple(map(int, arriba_der))
    
    cv2.rectangle(imagen, arriba_izq, abajo_der, (0,255,0), 2)

    cv2.putText(imagen, texto, arriba_izq, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    plt.imshow(imagen)
    plt.show()