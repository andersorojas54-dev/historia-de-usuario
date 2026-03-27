#service
def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parámetros:
        inventario (list): lista de productos
        nombre (str): nombre del producto
        precio (float): precio del producto
        cantidad (int): cantidad disponible

    Retorna:
        None
    """
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("Inventario vacío.")
        return
    
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.

    Retorna:
        dict o None
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza un producto existente.
    """
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)
    
    if producto:
        inventario.remove(producto)
        return True
    return False


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.

    Retorna:
        dict con métricas
    """
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }
    

# MÓDULO DE ARCHIVOS 
import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if not inventario:
        print("No hay datos para guardar.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar archivo:", e)


def cargar_csv(ruta):
    """
    Carga productos desde un CSV.

    Retorna:
        lista de productos y cantidad de errores
    """
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            header = next(reader)

            if header != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return [], 0

            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        return inventario, errores

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación.")
    except Exception as e:
        print("Error:", e)

    return [], 0

# APP PRINCIPAL



inventario = []

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Seleccione opción: ")

    try:
        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Buscar producto: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "Porducto No encontrado")

        elif opcion == "4":
            nombre = input("Producto: ")
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            actualizar_producto(
                inventario,
                nombre,
                float(precio) if precio else None,
                int(cantidad) if cantidad else None
            )

        elif opcion == "5":
            nombre = input("Eliminar: ")
            if eliminar_producto(inventario, nombre):
                print("Eliminado")
            else:
                print("No encontrado")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print(stats)
            else:
                print("Inventario vacío")

        elif opcion == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta archivo: ")
            nuevos, errores = cargar_csv(ruta)

            if nuevos:
                op = input("¿Sobrescribir? (Si/No): ").upper()

                if op == "S":
                    inventario = nuevos
                    accion = "reemplazo"
                else:
                    # fusión
                    for n in nuevos:
                        existente = buscar_producto(inventario, n["nombre"])
                        if existente:
                            existente["cantidad"] += n["cantidad"]
                            existente["precio"] = n["precio"]
                        else:
                            inventario.append(n)
                    accion = "fusión"

                print(f"Cargados: {len(nuevos)}, errores: {errores}, acción: {accion}")

        elif opcion == "9":
            print("Adiós ")
            break

        else:
            print("Opción inválida")

    except Exception as e:
        print("Error en la entrada:", e)
        
        
        
        
