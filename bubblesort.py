# Tipo de Algoritmo: Ordenación
# Nombre: Bubble Sort
# Funcionamiento: Trabaja repetidamente intercambiando el elemento adyacente en caso de que
# no se encuentre en el orden ascendente adecuado.
# Implementación: Ismael Flores - version python1.0 - 01 octubre 2022

def ordenaBurbuja(ArrayN):
    n = len(ArrayN)
    for i in range(n):
        for j in range(0, n-i-1):
            if ArrayN[j] > ArrayN[j+1]:
                ArrayN[j], ArrayN[j+1] = ArrayN[j+1], ArrayN[j]  
    print(ArrayN)   

if __name__ == "__main__":
    nn = input("Introduzca la longitud del arreglo: ")
    nn = int(nn)
    ArrayN = []
    elemento = 0
    for elemento in range(nn):
        new_el = input(f"Introduzca el numero para el elemento {elemento}: ")
        ArrayN.append(new_el)
    print("\n ++ SIN ORDENAR ++")
    print(ArrayN)
    print("\n ++ ORDENADO ++")
    ordenaBurbuja(ArrayN)
    