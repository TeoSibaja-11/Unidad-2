class InventarioTienda:
    def __init__(self, Nombre):
        self.Nombre= Nombre 
        self.productos = []  

    def agregar_producto(self, Nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print(" Precio y cantidad deben ser positivos")
            return
        for producto in self.productos:
            if producto["nombre"].lower() == Nombre.lower():
                producto["cantidad"] += cantidad
                print(f" Se agregaron {cantidad} unidades mas de {Nombre}")
                return
        
        self.productos.append({"nombre": Nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto '{Nombre}' agregado al inventario")

    def vender_producto(self, Nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == Nombre.lower():
                if cantidad <= 0:
                    print(" La cantidad debe ser positiva")
                    return
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print(f"Venta realizada: {cantidad} unidades de {Nombre}.")
                    if producto["cantidad"] == 0:
                        print(f"El producto '{Nombre}' se ha agotado")
                    return
                else:
                    print("No hay suficiente stock disponible")
                    return
        print(" El producto no existe en el inventario")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacio")
            return
        print(f"Inventario de {self.Nombre}:")
        for producto in self.productos:
            print(f"  {producto['nombre']} | Precio: ${producto['precio']:.2f} | Cantidad: {producto['cantidad']}")
        print()

    def producto_mas_caro(self):
        if not self.productos:
            print("No hay productos en el inventario")
            return
        producto_caro = max(self.productos, key=lambda p: p["precio"])
        print(f" El producto más caro es '{producto_caro['nombre']}' con un precio de {producto_caro['precio']:.2f}")


tienda = InventarioTienda("Tienda")

while True:
    print("---MENÚ DE OPCIONES---")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver el inventario")
    print("4. Consultar producto mas caro")
    print("5. Salir del programa")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        Nombre = input("Nombre del producto: ")
        try:
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad: "))
            tienda.agregar_producto(Nombre, precio, cantidad)
        except ValueError:
            print("El precio debe ser en numero y cantidad en entero")

    elif opcion == "2":
        Nombre = input("Nombre del producto a vender: ")
        try:
            cantidad = int(input("Cantidad a vender: "))
            tienda.vender_producto(Nombre, cantidad)
        except ValueError:
            print("Cantidad no esta en numero entero")

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        tienda.producto_mas_caro()

    elif opcion == "5":
        print("Saliendo del programa, GRACIAS...")
        break

    else:
        print("Opción incorrecta")
        print("Intente de nuevamente")