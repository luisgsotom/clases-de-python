print("✨¡Sean Bienvenidos al SGP, Gestione sus Productos de formma Rápida!")

inventario = []

while True:
    print("\n" + "- " * 25)
    print("📦 Panel Principal - Gestión de Inventario")
    print("- " * 25)
    print("1. Registrar nuevo artículo")
    print("2. Ver listado de artículos")
    print("3. Buscar en inventario")
    print("4. Quitar artículo")
    print("5. Salir del sistema")
    print("- " * 25)

    eleccion = input("\nElija una opción (1-5): ").strip()

    # Opción 1: agregar artículo
    if eleccion == "1":
        print("\n--- Registro de nuevo artículo ---")

        # Nombre
        titulo = ""
        while titulo == "":
            titulo = input("Ingrese el nombre del artículo: ").strip()
            if titulo == "":
                print("⚠️ El nombre no puede quedar vacío.")

        # Categoría
        tipo = ""
        while tipo == "":
            tipo = input("Ingrese la categoría: ").strip()
            if tipo == "":
                print("⚠️ La categoría no puede quedar vacía.")

        # Precio
        valor_str = ""
        while not valor_str.isdigit():
            valor_str = input("Ingrese el precio (solo números): ").strip()
            if not valor_str.isdigit():
                print("⚠️ Debe ingresar un número válido sin coma.")

        valor = int(valor_str)

        inventario.append([titulo, tipo, valor])
        print(f"\n✅ '{titulo}' fue agregado correctamente al inventario.")

    # Opción 2: mostrar artículos
    elif eleccion == "2":
        print("\n--- Listado de artículos disponibles ---")

        if len(inventario) == 0:
            print("No haz cargado ningun artículo en el inventario.")
        else:
            print(f"\nTotal de artículos: {len(inventario)}\n")
            indice = 1
            for item in inventario:
                print(f"{indice}. Nombre: {item[0]}")
                print(f"   Categoría: {item[1]}")
                print(f"   Precio: ${item[2]}")
                print("-" * 35)
                indice += 1

    # Opción 3: buscar artículo
    elif eleccion == "3":
        print("\n--- Búsqueda de artículos ---")

        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            termino = input("Ingrese el nombre o parte del nombre: ").strip().lower()

            if termino == "":
                print("⚠️ Ingrese un texto para buscar.")
            else:
                coincidencias = []
                indice = 1
                for item in inventario:
                    if termino in item[0].lower():
                        coincidencias.append([indice, item])
                    indice += 1

                if coincidencias:
                    print(f"\n🔍 Se encontraron {len(coincidencias)} resultado(s):\n")
                    for encontrado in coincidencias:
                        pos = encontrado[0]
                        art = encontrado[1]
                        print(f"{pos}. Nombre: {art[0]}")
                        print(f"   Categoría: {art[1]}")
                        print(f"   Precio: ${art[2]}")
                        print("-" * 35)
                else:
                    print(f"No se hallaron artículos con el término '{termino}'.")

    # Opción 4: eliminar artículo
    elif eleccion == "4":
        print("\n--- Eliminación de artículos ---")

        if len(inventario) == 0:
            print("No hay artículos registrados.")
        else:
            indice = 1
            for item in inventario:
                print(f"{indice}. {item[0]} (${item[2]})")
                indice += 1

            posicion_str = ""
            while not posicion_str.isdigit():
                posicion_str = input("\nIngrese el número del artículo a eliminar: ").strip()
                if not posicion_str.isdigit():
                    print("⚠️ Ingrese un número válido.")

            posicion = int(posicion_str)

            if 1 <= posicion <= len(inventario):
                item_eliminar = inventario[posicion - 1]
                confirm = input(f"¿Eliminar '{item_eliminar[0]}'? (s/n): ").strip().lower()
                if confirm == "s":
                    inventario.pop(posicion - 1)
                    print(f"\n🗑️ '{item_eliminar[0]}' fue eliminado del inventario.")
                else:
                    print("❎ Eliminación cancelada.")
            else:
                print(f"⚠️ Ingrese un número entre 1 y {len(inventario)}.")

    # Opción 5: salir
    elif eleccion == "5":
        print("\nGracias por usar el Gestor de Inventario. ¡Hasta la próxima!")
        break

    else:
        print("\n⚠️ Opción inválida. Por favor elija entre 1 y 5.")

    input("\nPresione Enter para continuar...")
