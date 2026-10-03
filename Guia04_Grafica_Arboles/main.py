import time
from pathlib import Path

import networkx as nx
import matplotlib.pyplot as plt


ARCHIVO = Path(__file__).with_name("arboles.txt")


def leer_arboles(ruta):
    """Lee dos árboles desde un archivo de texto.
    Cada línea de relación tiene el formato: nodo1-nodo2
    """
    arboles = []
    actual = None

    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea or linea.startswith("#"):
                if linea.startswith("# ARBOL"):
                    actual = nx.Graph()
                    arboles.append(actual)
                continue

            if actual is None:
                continue

            partes = [p.strip() for p in linea.split("-", 1)]
            if len(partes) == 2 and all(partes):
                actual.add_edge(partes[0], partes[1])

    return arboles


def altura_arbol(grafo):
    """Calcula la altura tomando como raíz el primer nodo."""
    if grafo.number_of_nodes() == 0:
        return 0

    raiz = next(iter(grafo.nodes))
    distancias = nx.single_source_shortest_path_length(grafo, raiz)
    return max(distancias.values())


def mostrar_reporte(grafo, numero):
    print(f"\n========== REPORTE DEL ÁRBOL {numero} ==========")
    print("Nodos:", ", ".join(grafo.nodes))
    print("Conexiones:")
    for origen, destino in grafo.edges:
        print(f"  {origen} <-> {destino}")

    print(f"\nCantidad de nodos: {grafo.number_of_nodes()}")
    print(f"Cantidad de conexiones: {grafo.number_of_edges()}")
    print(f"¿Es un árbol?: {'Sí' if nx.is_tree(grafo) else 'No'}")
    print(f"¿Está conectado?: {'Sí' if nx.is_connected(grafo) else 'No'}")
    print(f"Altura tomando como raíz el primer nodo: {altura_arbol(grafo)}")

    hojas = [n for n, grado in grafo.degree if grado == 1]
    print("Nodos hoja:", ", ".join(hojas) if hojas else "Ninguno")

    print("\nGrado de cada nodo:")
    for nodo, grado in grafo.degree:
        print(f"  {nodo}: {grado}")


def graficar(grafo, numero):
    plt.figure(figsize=(10, 6))
    posicion = nx.spring_layout(grafo, seed=42)
    nx.draw(
        grafo,
        posicion,
        with_labels=True,
        node_size=2200,
        font_size=9,
        font_weight="bold",
    )
    plt.title(f"Gráfica del Árbol {numero}")
    plt.tight_layout()
    nombre = f"arbol_{numero}.png"
    plt.savefig(nombre, dpi=180, bbox_inches="tight")
    plt.show()
    print(f"Imagen guardada como: {nombre}")


def buscar_nodo(grafo, numero):
    consulta = input(f"Ingrese el nodo que desea consultar en el Árbol {numero}: ").strip()

    if consulta not in grafo:
        print("El nodo no existe en este árbol.")
        return

    print(f"\nNodo encontrado: {consulta}")
    print("Vecinos/conexiones:", ", ".join(grafo.neighbors(consulta)) or "Sin conexiones")
    print("Grado:", grafo.degree[consulta])


def medir_tiempo(arboles):
    inicio = time.perf_counter_ns()

    for grafo in arboles:
        nx.is_tree(grafo)
        list(grafo.nodes)
        list(grafo.edges)
        for nodo in grafo.nodes:
            _ = list(grafo.neighbors(nodo))

    fin = time.perf_counter_ns()
    tiempo_ns = fin - inicio
    print("\n========== ANÁLISIS DE TIEMPO ==========")
    print(f"Tiempo de procesamiento: {tiempo_ns} ns")
    print(f"Tiempo de procesamiento: {tiempo_ns / 1_000_000:.6f} ms")
    print("Nota: el valor puede variar según el computador y la ejecución.")


def main():
    print("==============================================")
    print(" GUÍA DE PRÁCTICAS #04 - GRÁFICA DE ÁRBOLES")
    print("==============================================")

    arboles = leer_arboles(ARCHIVO)

    if len(arboles) < 2:
        raise ValueError("El archivo debe contener dos árboles.")

    print(f"\nSe cargaron {len(arboles)} árboles desde: {ARCHIVO.name}")

    while True:
        print("""
MENÚ PRINCIPAL
1. Mostrar reporte del Árbol 1
2. Mostrar reporte del Árbol 2
3. Graficar Árbol 1
4. Graficar Árbol 2
5. Consultar un nodo del Árbol 1
6. Consultar un nodo del Árbol 2
7. Medir tiempo de ejecución
8. Mostrar ambos reportes
0. Salir
""")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_reporte(arboles[0], 1)
        elif opcion == "2":
            mostrar_reporte(arboles[1], 2)
        elif opcion == "3":
            graficar(arboles[0], 1)
        elif opcion == "4":
            graficar(arboles[1], 2)
        elif opcion == "5":
            buscar_nodo(arboles[0], 1)
        elif opcion == "6":
            buscar_nodo(arboles[1], 2)
        elif opcion == "7":
            medir_tiempo(arboles)
        elif opcion == "8":
            mostrar_reporte(arboles[0], 1)
            mostrar_reporte(arboles[1], 2)
        elif opcion == "0":
            print("Programa finalizado correctamente.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
