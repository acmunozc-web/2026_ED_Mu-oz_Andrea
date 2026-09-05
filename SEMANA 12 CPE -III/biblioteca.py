import time


# ==========================================================
# APLICACIÓN PARA EL REGISTRO DE LIBROS DE UNA BIBLIOTECA
# ==========================================================

# ----------------------------------------------------------
# ESTRUCTURA PRINCIPAL: DICCIONARIO
# ISBN -> información completa del libro
# ----------------------------------------------------------

libros = {}


# ----------------------------------------------------------
# CONJUNTO
# Almacena categorías sin permitir categorías repetidas
# ----------------------------------------------------------

categorias = set()


# ----------------------------------------------------------
# MAPA
# Relaciona el título del libro con su ISBN
# ----------------------------------------------------------

mapa_titulos = {}


# ==========================================================
# FUNCIÓN PARA REGISTRAR UN LIBRO
# ==========================================================

def registrar_libro():

    print("\n===================================")
    print("        REGISTRO DE LIBRO")
    print("===================================")

    isbn = input("Ingrese el ISBN: ").strip()

    # Verificar si el ISBN ya existe
    if isbn in libros:
        print("\nERROR: Ya existe un libro con ese ISBN.")
        return

    titulo = input("Ingrese el título: ").strip()
    autor = input("Ingrese el autor: ").strip()
    anio = input("Ingrese el año de publicación: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    respuesta = input(
        "¿El libro está disponible? (s/n): "
    ).strip().lower()

    disponible = respuesta == "s"

    # Crear el registro del libro
    libros[isbn] = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "categoria": categoria,
        "disponible": disponible
    }

    # Agregar categoría al conjunto
    categorias.add(categoria)

    # Crear relación título -> ISBN
    mapa_titulos[titulo.lower()] = isbn

    print("\nLibro registrado correctamente.")


# ==========================================================
# CONSULTAR LIBRO POR ISBN
# ==========================================================

def consultar_libro():

    print("\n===================================")
    print("        CONSULTAR LIBRO")
    print("===================================")

    isbn = input("Ingrese el ISBN: ").strip()

    if isbn not in libros:
        print("\nNo se encontró un libro con ese ISBN.")
        return

    libro = libros[isbn]

    print("\nInformación del libro")
    print("-----------------------------------")
    print("ISBN:", isbn)
    print("Título:", libro["titulo"])
    print("Autor:", libro["autor"])
    print("Año:", libro["anio"])
    print("Categoría:", libro["categoria"])

    if libro["disponible"]:
        print("Estado: Disponible")
    else:
        print("Estado: No disponible")


# ==========================================================
# BUSCAR LIBRO POR TÍTULO
# ==========================================================

def buscar_por_titulo():

    print("\n===================================")
    print("       BUSCAR POR TÍTULO")
    print("===================================")

    titulo = input("Ingrese el título: ").strip().lower()

    if titulo in mapa_titulos:

        isbn = mapa_titulos[titulo]
        libro = libros[isbn]

        print("\nLibro encontrado")
        print("-----------------------------------")
        print("ISBN:", isbn)
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        print("Categoría:", libro["categoria"])

        if libro["disponible"]:
            print("Estado: Disponible")
        else:
            print("Estado: No disponible")

    else:
        print("\nNo se encontró un libro con ese título.")


# ==========================================================
# MOSTRAR TODOS LOS LIBROS
# ==========================================================

def mostrar_libros():

    print("\n===================================")
    print("        REPORTE DE LIBROS")
    print("===================================")

    if not libros:
        print("No existen libros registrados.")
        return

    for isbn, libro in libros.items():

        print("\n-----------------------------------")
        print("ISBN:", isbn)
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        print("Categoría:", libro["categoria"])

        if libro["disponible"]:
            print("Estado: Disponible")
        else:
            print("Estado: No disponible")


# ==========================================================
# MOSTRAR CATEGORÍAS
# ==========================================================

def mostrar_categorias():

    print("\n===================================")
    print("       CATEGORÍAS REGISTRADAS")
    print("===================================")

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print("-", categoria)


# ==========================================================
# MOSTRAR ESTADÍSTICAS
# ==========================================================

def mostrar_estadisticas():

    print("\n===================================")
    print("           ESTADÍSTICAS")
    print("===================================")

    total_libros = len(libros)

    disponibles = sum(
        1
        for libro in libros.values()
        if libro["disponible"]
    )

    no_disponibles = total_libros - disponibles

    print("Total de libros:", total_libros)
    print("Libros disponibles:", disponibles)
    print("Libros no disponibles:", no_disponibles)
    print("Cantidad de categorías:", len(categorias))


# ==========================================================
# ANALIZAR TIEMPO DE EJECUCIÓN
# ==========================================================

def medir_tiempo():

    print("\n===================================")
    print("     ANÁLISIS DEL TIEMPO")
    print("===================================")

    inicio = time.perf_counter()

    # Recorrido del diccionario
    for isbn in libros:
        _ = libros[isbn]

    fin = time.perf_counter()

    tiempo = fin - inicio

    print(
        f"Tiempo de recorrido: "
        f"{tiempo:.10f} segundos"
    )


# ==========================================================
# MENÚ PRINCIPAL
# ==========================================================

def menu():

    while True:

        print("\n")
        print("==========================================")
        print("   SISTEMA DE REGISTRO DE BIBLIOTECA")
        print("==========================================")
        print("1. Registrar libro")
        print("2. Consultar libro por ISBN")
        print("3. Buscar libro por título")
        print("4. Mostrar todos los libros")
        print("5. Mostrar categorías")
        print("6. Mostrar estadísticas")
        print("7. Analizar tiempo de ejecución")
        print("8. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_libro()

        elif opcion == "2":
            consultar_libro()

        elif opcion == "3":
            buscar_por_titulo()

        elif opcion == "4":
            mostrar_libros()

        elif opcion == "5":
            mostrar_categorias()

        elif opcion == "6":
            mostrar_estadisticas()

        elif opcion == "7":
            medir_tiempo()

        elif opcion == "8":
            print("\nPrograma finalizado correctamente.")
            break

        else:
            print("\nOpción no válida.")


# ==========================================================
# INICIO DEL PROGRAMA
# ==========================================================

menu()