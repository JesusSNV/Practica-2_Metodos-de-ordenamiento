# ORDENAMIENTO POR MEZCLA DIRECTA (Straight Merging)

def mezcla_directa(arr):
    #Sí el arreglo tiene más de un elemtno, se divide en dos mitades
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        #Se ordena cada mitad
        mezcla_directa(izquierda)
        mezcla_directa(derecha)

        #Se mezclan las dos mitades ordenadas
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            #Compara elementos de ambas mitades y coloca el menor
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        #Copia los elementos restantes de la izquierda
        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        #Copia los elementos restantes de la derecha
        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

    return arr


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Mezcla Directa:", mezcla_directa(datos.copy()))