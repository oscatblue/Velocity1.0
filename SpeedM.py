# -*- coding: utf-8 -*-

import time, random
#123
#otro cambio
from datetime import datetime, date


inicio = time.strftime("%Y%m%d")
fin="1_1_12345_99"
abc=['A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
placa=""
placa_anterior="818GVG"
for i in range (0,50):
    volado=random.randint(1,20)
    if volado % 3 ==  0:
        placa=placa_anterior
    else:
        for i in range(1,4,1):
            c=random.randint(0,22)
            placa= placa+abc[c]
        for i in range(1,4,1):
            n=random.randint(0,9)
            placa= placa+str(n)
    P=inicio+'_'+time.strftime("%H%M%S")+'_'+placa+'_'+fin
    if random.randint(1,50)% 3 == 0:
        minutos=int(P[11:13])+5
        hora=P[9:11]
        if minutos > 59:
            minutos=minutos-60
            minutos=str(minutos)
            if int (minutos)  < 10:
                minutos='0'+minutos
                hora=int(hora)+1
                hora=str(hora)
        print hora
       # hora=hora+1

        P=P[0:9]+str(hora)+str(minutos)+P[13:]
    print P
    p=open("C:\Users\Dell\Desktop\generados\placas\\"+ P+'.jpg', 'w')
    placa_anterior=placa
    placa=""
    time.sleep(random.randint(1,5))
