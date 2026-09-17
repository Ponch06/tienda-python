
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:49:04 2026

@author: ponch
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:49:04 2026

@author: ponch
"""

print("¿Qué descuento deseas aplicar?")
print("1. Descuento del 10%")
print("2. Promoción 3x2")

opcion = input("Selecciona una opción: ")
    
if opcion == "1":
    subtotal = float(input("Ingresa el subtotal: "))
    descuento = subtotal * 0.10
    total = subtotal - descuento

    print("Descuento aplicado:", descuento)
    print("Total a pagar:", total)

elif opcion == "2":
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("¿Cuántos productos compraste?: "))

    if cantidad >= 3:
        grupos = cantidad // 3
        sobrantes = cantidad % 3

        pagados = (grupos * 2) + sobrantes
        total = pagados * precio

        print("Promoción 3x2 aplicada")
        print("Total a pagar:", total)

    else:
        total = cantidad * precio
        print("No aplica la promoción 3x2")
        print("Total a pagar:", total)

else:
    print("Opción no válida")