def generar_ticket(carrito, catalogo, total):
    folio = "F001"
    fecha = "2026-09-09"

    ticket = (folio, fecha, total)

    print("\n===== TICKET =====")
    print("Folio:", ticket[0])
    print("Fecha:", ticket[1])
    print("Total: $", ticket[2])

    return ticket 