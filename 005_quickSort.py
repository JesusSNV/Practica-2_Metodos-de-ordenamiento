# ORDENAMIENTO RÁPIDO (QuickSort)

def quick_sort(arr):
    #Sí hay listas vacías o de solo un elemento
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2] #centro
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    #Ordena recursivamente menores y mayores
    return quick_sort(menores) + iguales + quick_sort(mayores)


if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    print("Quick Sort:", quick_sort(datos.copy()))
