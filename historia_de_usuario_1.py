# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")
# Validar el precio 
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo. Intente nuevamente.")
        else:
            break
    except:
        print("Entrada inválida. Debe ingresar un número.")

# Validar la cantidad 
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Intente nuevamente.")
        else:
            break
    except:
        print("Entrada inválida. Debe ingresar un número entero.")


# Calcular el costo total
costo_total = precio * cantidad

#Resultados
print("\n===== RESULTADO DEL INVENTARIO =====")
print("Producto:", nombre)
print("Precio unitario:", precio)
print("Cantidad:", cantidad)
print("Costo total:", costo_total)
