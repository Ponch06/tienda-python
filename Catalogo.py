# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:57:49 2026

@author: Citlali
"""


def cargar_catalogo():
    # Usamos un diccionario donde la clave es el ID del producto
    catalogo = {
        "P001": {"nombre": "Café", "precio": 45.0, "stock": 20},
        "P002": {"nombre": "Galletas", "precio": 15.0, "stock": 30},
        "P003": {"nombre": "Leche", "precio": 25.0, "stock": 15},
        "P004": {"nombre": "Azúcar", "precio": 20.0, "stock": 10} #
    }
    return catalogo

def mostrar_catalogo(catalogo):
    """
    Imprime una tabla con los productos disponibles recorriendo el diccionario.
    """
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    print(f"{'ID':<6} | {'Nombre':<15} | {'Precio':<8} | {'Stock'}")
    print("-" * 45)
    
    # Iteración obligatoria con 'for'
    for id_prod, info in catalogo.items():
        print(f"{id_prod:<6} | {info['nombre']:<15} | ${info['precio']:<7.2f} | {info['stock']}")
    print("-" * 45)