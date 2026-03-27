import json
#Lista
inventario = []

# Agregar producto
def agregar_producto():
    nombre = input("Nombre del producto: ")

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except:
        print("Error: debes ingresar números válidos\n")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)

    print("Producto agregado correctamente\n")

#Mostrar inventario
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío\n")
    else:
        print("\n--- INVENTARIO ---")
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
        print()

#Calcular estadísticas
def calcular_estadisticas():
    if len(inventario) == 0:
        print("No hay productos\n")
        return

    valor_total = 0
    total_productos = 0

    for p in inventario:
        valor_total = valor_total + (p["precio"] * p["cantidad"])
        total_productos = total_productos + p["cantidad"]

    print("\n--- ESTADÍSTICAS ---")
    print("Valor total del inventario:", valor_total)
    print("Cantidad total de productos:", total_productos)
    print()

#Guardar en JSON
def guardar_json():
    if len(inventario) == 0:
        print("No hay datos para guardar\n")
        return

    try:
        archivo = open("inventario.json", "w", encoding="utf-8")
        json.dump(inventario, archivo, indent=4)
        archivo.close()
        print("Inventario guardado en inventario.json\n")
    except:
        print("Error al guardar archivo\n")

# Cargar json
def cargar_json():
    global inventario

    try:
        archivo = open("inventario.json", "r", encoding="utf-8")
        inventario = json.load(archivo)
        archivo.close()
        print("Inventario cargado correctamente\n")
    except:
        print("Error al cargar archivo\n")

# MENÚ PRINCIPAL
def mostrar_menu():
    print("===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Guardar en JSON")
    print("5. Cargar desde JSON")
    print("6. Salir")

# PROGRAMA PRINCIPAL
def ejecutar_programa():
    salir = False

    while salir == False:
        mostrar_menu()

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            mostrar_inventario()

        elif opcion == "3":
            calcular_estadisticas()

        elif opcion == "4":
            guardar_json()

        elif opcion == "5":
            cargar_json()

        elif opcion == "6":
            print("Saliendo del programa...")
            salir = True

        else:
            print("Opción inválida, intenta otra vez\n")



ejecutar_programa()
