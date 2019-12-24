import os
import random
import time
print('BANG!!!!!\n E LÁ VÃO ELES!!!!!')

pista = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
i = 0
tartaruga = 1
lebre = 1
while tartaruga <= 70 and lebre <= 70:
    pista[lebre] = 'L' 
    pista[tartaruga] = 'T'
    print(*pista)
    pista = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
    i = random.randint(1, 10)
    if i >= 1 and i <= 5:
        tartaruga += 3
    elif i >= 6 and i <= 7:
        tartaruga -= 6
    elif i >= 8 and i <= 10:
        tartaruga += 1  
    if i >= 1 and i <= 2:
        lebre += 0
    elif i >= 3 and i <= 4:
        lebre += 9
    elif i == 5:
        lebre -= 12
    elif i >= 6 and i <= 8:
        lebre += 1
    elif i >= 9 and i <= 10:
        lebre += 2
    if tartaruga <= 0:
        tartaruga = 0
    if lebre <= 0:
        lebre = 0
    if tartaruga >= 70:
        print('TARTARUGA VENCE!!! É ISSO AÍ!!!')
        break
    if lebre >= 70:
        print('Lebre vence. Marmelada')
        break
    if lebre >= 70 and tartaruga >= 70:
        print('É UM EMPATE')
        break
    if tartaruga == lebre:
        pista[lebre] = 'AI'


    time.sleep(0.25)
    os.system('cls')