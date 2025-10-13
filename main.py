print("¡Sean Bienvenidos y A al Sistema de Gestion de Productos!")

productos = []

while True:
    print("\n" + "="*40) # ======================================
    print("Sistema de Gestion de Productos") # Sistema de Gestion de Productos
    print("="*40) # ==========================================
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("="*40) # ==========================================

    opcion = input("\nSeleccione una opcion (1-5): ").strip()
    
    # Agregar producto
    if opcion == "1":
        print("\n --- Agregar producto ---")
        
        # Validar nombre
        nombre = ""
        while nombre == "":
            nombre = input("Ingrese el nombre del producto: ").strip()
            if nombre == "":
                print("Error: el nombre no puede estar vacio.")
        
        # Validar categoria
        categoria = ""
        while categoria == "":
            categoria = input("Ingrese la categoria del producto: ").strip()
            if categoria == "":
                print("Error: la categoria no puede estar vacio.")
                
        # Validar precio
        precio_str = ""
        while not precio_str.isdigit():
            precio_str = input("Ingrese el precio del producto (solo números): ").strip()
            if not precio_str.isdigit():
                print("Error: debe ingresar un numero valido sin coma")
        
        precio = int(precio_str)

        productos.append([nombre,categoria,precio])
        print(f"\n ✅Producto '{nombre}' agregado exitosamente!")
        
    # Mostrar poductos    
    elif opcion == "2":
        print("\n --- Productos Registrados ---")
        
        if len(productos) == 0:
            print("No hay productos registrado en nuestra tienda")
        else:
            print(f"\nTotal de productos: {len(productos)} \n")
            
            contador = 1
            for producto in productos:        
                nombre = producto[0]
                categoria = producto[1]
                precio = producto[2]
                print(f"{contador}. Nombre: {nombre}")
                print(f"    Categoria: {categoria}")
                print(f"    Precio: {precio}")
                print("-"*30)
                contador += 1 
    
    # Buscar producto
    elif opcion == "3":
        print("\n --- Buscar Producto ---")
        
        if len(productos) == 0:
            print("No hay productos para buscar")
        else:
            busqueda = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            
            if busqueda == "":
                print("Error: debe ingresar un nombre.")
            else:
                encontrados = []
                contador = 1
                for producto in productos:
                    nombre = producto[0].lower()
                    if busqueda in nombre: 
                        encontrados.append([contador,producto])
                    contador += 1
                
                if len(encontrados) > 0:
                    print(f"\n Se encontraron {len(encontrados)} coincidencia(s): \n")
                    for elemento in encontrados:
                        posicion = elemento[0]
                        producto = elemento[1]
                        print(f"{posicion}. Nombre: {producto[0]}")
                        print(f"   Categoría: {producto[1]}")
                        print(f"   Precio: ${producto[2]}")
                        print("-" * 30)
                else:
                    print(f"\nNo se encontraron productos que coincidan con '{busqueda}'.")
    
    # Eliminar producto             
    elif opcion == "4":
        print("\n--- Eliminar Producto ---")

        if len(productos) == 0:
            print("No hay productos registrados en el sistema.")
        else:
            # Mostrar productos
            contador = 1
            for producto in productos:
                print(f"{contador}. {producto[0]} (${producto[2]})")
                contador += 1
                

            posicion_str = ""
            while not posicion_str.isdigit():
                posicion_str = input("\nIngrese el número del producto a eliminar: ").strip()  
                if not posicion_str.isdigit():
                    print("Error: debe ingresar un número válido.")

            posicion = int(posicion_str)

            if 1 <= posicion <= len(productos):
                producto_eliminar = productos[posicion - 1]
                confirmacion = input(f"¿Está seguro que desea eliminar '{producto_eliminar[0]}'? (s/n): ").strip().lower()
                if confirmacion == "s":
                    productos.pop(posicion - 1)
                    print(f"\n✓ Producto '{producto_eliminar[0]}' eliminado exitosamente.")
                else:
                    print("\nEliminación cancelada.")
            else:
                print(f"Error: debe ingresar un número entre 1 y {len(productos)}.")

    # -----------------------------------------
    # OPCIÓN 5: SALIR
    # -----------------------------------------
    elif opcion == "5":
        print("\n¡Gracias por usar el sistema! Hasta pronto.")
        break        
    
    else:
        print("\n Error: opcion invalida. por favor elegi una opcion entre 1 al 5")
    
    input("\n Presione enter para continuar...")