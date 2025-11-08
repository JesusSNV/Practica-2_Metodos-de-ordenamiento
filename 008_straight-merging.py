# ORDENAMIENTO POR MEZCLA DIRECTA (Straight Merging)

def mezcla_directa(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        mezcla_directa(izquierda)
        mezcla_directa(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Mezcla Directa:", mezcla_directa(datos.copy()))