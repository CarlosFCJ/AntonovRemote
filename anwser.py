# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 09:17:07 2020

@author: CarlosC
"""
c = 20
while c!=0:
    kg=int(input("Ingrese el peso en kilogramos del paquete que desea enviar :"))
    km=int(input("ingrese la distancia en kilometos a la cual se dirije el paquete :"))
    N=int(input("ingrese 1 si el paquete realiza un viaje nacional y 2 si realiza un viaje internacional :"))
    if kg>=10 :
        if N==1 :
            p = (kg*4500) + (km*4000)
            if N>100 :
                p = (p*15)/100
        else :
            mi = km/1.609
            p = (kg*4500) + (mi*8000)
            if km>800 and kg>400 :
                p = (p*10)/100
        c = c-kg
        if c<0 :
            print("Paquete no valido, sobrepasa el cupo de la nave")
        else :
            print("el valor a pagar es" + str(p))
    else :
        print("el peso del paquete no pasaa el minimo de 10 kg pedido por la empresa")
print("el avion esta lleno")