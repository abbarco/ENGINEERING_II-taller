# Crear un diccionario para almacenar el menú con sus precios
menu = {
    'langosta': 25,
    'costillas asadas': 13,
    'pollo a la parrilla': 10,
    'pizza margarita': 8,
    'sopa de tomate': 5,
    'pastel de chocolate': 6,
    'salchipapa': 3,
    'especial del chef 1': 15,
    'especial del chef 2': 20
}

# Función para mostrar el menú y permitir al usuario seleccionar los platos y cantidades
def seleccionar_menu():
    print("Menú:")
    for plato, precio in menu.items():
        print(f"{plato}: ${precio}")

    orden = {}
    while True:
        plato = input("\nSelecciona un plato del menú (escribe 'fin' para terminar): ")
        if plato.lower() == 'fin':
            break

        if plato.lower() not in menu:
            print("Plato no disponible en el menú. Inténtalo de nuevo.")
            continue

        cantidad = input("Ingresa la cantidad de platos que deseas: ")
        try:
            cantidad = int(cantidad)
            if cantidad <= 0 or cantidad > 100:
                print("La cantidad debe ser un número positivo mayor que cero y menor o igual a 100.")
                continue
        except ValueError:
            print("Ingresa un número válido para la cantidad.")
            continue

        orden[plato] = cantidad

    return orden

# Función para calcular el costo total de la orden
def calcular_costo(orden):

    if not bool(orden):
        return -1

    costo_total = 0
    total_platos = 0

    for plato, cantidad in orden.items():
        costo_plato = menu[plato] * cantidad
        costo_total += costo_plato
        total_platos += cantidad

    if total_platos > 5 and total_platos < 10:
        costo_total *= 0.9  # Aplicar descuento del 10% si hay más de 5 platos
    if total_platos > 10:
        costo_total *= 0.8  # Aplicar descuento del 20% si hay más de 10 platos

    # Aplicar descuentos especiales
    if costo_total > 100:
        costo_total -= 25
    elif costo_total > 50:
        costo_total -= 10

    # Aplicar recargo del 5% para los Chef's Specials
    if any(plato.startswith("especial") for plato in orden.keys()):
        costo_total *= 1.05

    return costo_total

# Función principal para gestionar la experiencia de comedor
def dining_experience_manager():
    orden = seleccionar_menu()
    if not orden:
        print("\n¡Orden cancelada!")
        return -1

    costo_total = calcular_costo(orden)

    # Mostrar la orden y el costo total para confirmación del usuario
    print("\nResumen de la orden:")
    for plato, cantidad in orden.items():
        print(f"{plato}: ${menu[plato]} x {cantidad} = ${cantidad*menu[plato]}")

    print(f"Aplicar descuentos\nCOSTO TOTAL: ${costo_total}")

    confirmacion = obtener_respuesta_valida()
    if confirmacion == 'si':
        return costo_total
    else:
        print("¡Orden cancelada!")
        return -1

# Función para obtener una respuesta válida (si/no) del usuario
def obtener_respuesta_valida():
    while True:
        respuesta = input("\n¿Deseas confirmar la orden? (si/no): ").lower()
        if respuesta in ['si', 'no']:
            return respuesta
        else:
            print("Respuesta inválida. Por favor, ingresa 'si' o 'no'.")


# Ejecutar la función principal
if __name__ == "__main__":
    costo_dining_experience = dining_experience_manager()
    print(f"\nEl costo total de la experiencia de comedor es: ${costo_dining_experience}")
