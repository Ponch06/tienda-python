# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 09:33:26 2026

@author: 52244
"""
    ticket = (folio, fecha, total)

    print("\n========== TICKET ==========")
    print("Folio:", folio)
    print("Fecha:", fecha)
    print("----------------------------")

    for id_producto, cantidad in carrito.items():
        nombre = catalogo[id_producto]["nombre"]
        precio = catalogo[id_producto]["precio"]
        importe = precio * cantidad

        print(nombre, "x", cantidad, "=", "$", importe)

    print("----------------------------")
    print("TOTAL: $", total)

    return ticket