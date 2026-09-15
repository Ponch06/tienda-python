def agregar_carrito(catalogo, carrito):
    id_prod = input("Ingresa el ID del producto: ").upper()

    if id_prod not in catalogo:
        print("Ese producto no existe.")
        return

    cantidad = int(input("Ingresa la cantidad: "))

    if cantidad <= 0:
        print("La cantidad debe ser mayor que 0.")
        return

    if cantidad > catalogo[id_prod]["stock"]:
        print("No hay suficiente stock.")
        return

    # Agregamos una tupla a la lista
    carrito.append((id_prod, cantidad))

    print("Producto agregado al carrito.")


def mostrar_carrito(catalogo, carrito):
    print("\n--- CARRITO DE COMPRAS ---")

    if len(carrito) == 0:
        print("El carrito está vacío.")
        return

    total = 0

    for id_prod, cantidad in carrito:
        nombre = catalogo[id_prod]["nombre"]
        precio = catalogo[id_prod]["precio"]

        subtotal = precio * cantidad
        total += subtotal

        print(f"{nombre} | ${precio:.2f} x {cantidad} = ${subtotal:.2f}")

    print("-" * 40)
    print(f"Total: ${total:.2f}")


# PROGRAMA PRINCIPAL

catalogo = cargar_catalogo()

# El carrito es una lista de tuplas
carrito = []

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar catálogo")
    print("2. Agregar producto al carrito")
    print("3. Mostrar carrito")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_catalogo(catalogo)

    elif opcion == "2":
        mostrar_catalogo(catalogo)
        agregar_carrito(catalogo, carrito)

    elif opcion == "3":
        mostrar_carrito(catalogo, carrito)

    elif opcion == "4":
        print("Gracias por su compra.")
        break

    else:
        print("Opción no válida.")