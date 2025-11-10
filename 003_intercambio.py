# ORDENAMIENTO POR INTERCAMBIO (Bubble Sort)

def bubble_sort(arr):
    n = len(arr)
    #Recorre la lista varias veces
    for i in range(n):
        #Los elementos más grandes van al final
        for j in range(0, n - i - 1):
            #Intercambio so el actual es más grande que le anterior
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    print("Bubble Sort:", bubble_sort(datos.copy()))
