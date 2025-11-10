# ORDENAMIENTO POR INSERCIÓN (Insertion Sort)

def insertion_sort(arr):
    # Recorre desde el segundo elemento hasta el final
    for i in range(1, len(arr)):
        clave = arr[i]       # Elemento a insertar
        j = i - 1            # Índice del elemento anterior

        # Desplaza los elementos mayores que la clave una posición adelante
        while j >= 0 and arr[j] > clave:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserta la clave en la posición correcta
        arr[j + 1] = clave
    return arr


if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    print("Insertion Sort:", insertion_sort(datos.copy()))
