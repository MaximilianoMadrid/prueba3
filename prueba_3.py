import json
import os
from datetime import datetime

fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ventas = []

p_pizzas = {
    "margarita": {"pequeña": 5500, 
                  "mediana": 8500, 
                  "familiar": 11000},
    "mexicana": {"pequeña": 7000,
                 "mediana": 10000,
                 "familiar": 13000},
    "barbacoa": {"pequeña":6500,
                 "mediana": 9500,
                 "familiar": 12500},
    "vegetariana": {"pequeña": 5000,
                    "mediana": 8000,
                    "familiar": 10500}
}

def menu():
    print("\nBienvenido a Pizzas DUOC")
    print("Por favor, seleccione una opción:")
    print("1- Registrar una venta")
    print("2- Anular venta")
    print("3- Mostrar todas las ventas")
    print("4- Buscar ventas por cliente")
    print("5- Guardar ventas")
    print("6- Cargar ventas")
    print("7- Generar boleta")
    print("8- Salir")
    op = input("Seleccione una opción: ")
    return op

def registrar_venta():
    n_cliente = input("Nombre del cliente: ")
    t_cliente = input("Tipo de cliente (diurno/vespertino/administrativo): ").lower()
    t_pizza = input("Tipo de pizza (margarita/mexicana/barbacoa/vegetariana): ").lower()
    tamaño_pizza = input("Tamaño de la pizza (pequeña/mediana/familiar): ").lower()
    cant = int(input("Cantidad de pizzas: "))

    if t_pizza not in p_pizzas or tamaño_pizza not in p_pizzas[t_pizza]:
        print("Tipo o tamaño de pizza inválido.")
        return

    p_unitario = p_pizzas[t_pizza][tamaño_pizza]

    descuento = 0
    if t_cliente == 'diurno':
        descuento = 0.15
    elif t_cliente == 'vespertino':
        descuento = 0.18
    elif t_cliente == 'administrativo':
        descuento = 0.11

    p_total = p_unitario * cant
    p_final = p_total * (1 - descuento)

    venta = {
        "fecha_hora": fecha_hora,
        "nombre_cliente": n_cliente,
        "tipo_cliente": t_cliente,
        "tipo_pizza": t_pizza,
        "tamaño_pizza": tamaño_pizza,
        "cantidad": cant,
        "precio_unitario": p_unitario,
        "precio_total": p_total,
        "descuento": descuento,
        "precio_final": p_final
    }

    ventas.append(venta)
    print("\nVenta registrada exitosamente:")
    print(f"Fecha y hora: {fecha_hora}")
    print(f"Cliente: {n_cliente}")
    print(f"Tipo de cliente: {t_cliente}")
    print(f"Tipo de pizza: {t_pizza}")
    print(f"Tamaño de pizza: {tamaño_pizza}")
    print(f"Cantidad: {cant}")
    print(f"Precio unitario: {p_unitario}")
    print(f"Precio total: {p_total}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Precio final: {p_final}")

def anular_venta():
    cliente = input("Ingrese el nombre del cliente para anular su venta: ")
    global ventas
    ventas_anuladas = [venta for venta in ventas if venta["nombre_cliente"] == cliente]

    if not ventas_anuladas:
        print(f"No se encontraron ventas para el cliente '{cliente}'. No se realizó ninguna anulación.")
        return

    for venta in ventas_anuladas:
        ventas.remove(venta)

    print(f"Ventas de '{cliente}' anuladas correctamente.")

def mostrar_ventas():
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for idx, venta in enumerate(ventas, 1):
            print(f"\n--- Detalles de la Venta {idx} ---")
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Cliente: {venta['nombre_cliente']}")
            print(f"Tipo de cliente: {venta['tipo_cliente']}")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño de pizza: {venta['tamaño_pizza']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio unitario: {venta['precio_unitario']}")
            print(f"Precio total: {venta['precio_total']}")
            print(f"Descuento aplicado: {venta['descuento'] * 100}%")
            print(f"Precio final: {venta['precio_final']}")

def buscar_ventas():
    n_cliente = input("Ingrese el nombre del cliente a buscar: ")
    ventas_cliente = [venta for venta in ventas if venta["nombre_cliente"] == n_cliente]

    if not ventas_cliente:
        print(f"No se encontraron ventas para el cliente '{n_cliente}'.")
    else:
        for idx, venta in enumerate(ventas_cliente, 1):
            print(f"\n--- Detalles de la Venta {idx} ---")
            print(f"Fecha y hora: {venta['fecha_hora']}")
            print(f"Cliente: {venta['nombre_cliente']}")
            print(f"Tipo de cliente: {venta['tipo_cliente']}")
            print(f"Tipo de pizza: {venta['tipo_pizza']}")
            print(f"Tamaño de pizza: {venta['tamaño_pizza']}")
            print(f"Cantidad: {venta['cantidad']}")
            print(f"Precio unitario: {venta['precio_unitario']}")
            print(f"Precio total: {venta['precio_total']}")
            print(f"Descuento aplicado: {venta['descuento'] * 100}%")
            print(f"Precio final: {venta['precio_final']}")

def guardar_ventas():
    with open('ventas.json', 'w') as file:
        json.dump(ventas, file, indent=4)
    print("Ventas guardadas en 'ventas.json'.")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as file:
            ventas = json.load(file)
        print("Ventas cargadas desde 'ventas.json'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'ventas.json'.")

def generar_boleta():
    global ventas
    if not ventas:
        print("No hay ventas registradas para generar boleta.")
        return

    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subtotal = sum(venta["precio_final"] for venta in ventas)
    descuento = sum(venta["precio_total"] * venta["descuento"] for venta in ventas)
    total = subtotal - descuento

    boleta = f'''
    Boleta electrónica

    ************* Pizzas DUOC ***************

    Fecha: {fecha_hora_actual}

    Local: Alameda

    Dirección: Avenida España 8, Santiago, RM

    -----------------------------------------
    Subtotal         ${subtotal:.2f}
    Descuento        ${descuento:.2f}
    -----------------------------------------
    Total a pagar    ${total:.2f}

    ********** ¡Gracias por su compra! **********
    '''

    print(boleta)

def main():
    while True:
        op = menu()
        if op == '1':
            registrar_venta()
        elif op == '2':
            anular_venta()
        elif op == '3':
            mostrar_ventas()
        elif op == '4':
            buscar_ventas()
        elif op == '5':
            guardar_ventas()
        elif op == '6':
            cargar_ventas()
        elif op == '7':
            generar_boleta()
        elif op == '8':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()

