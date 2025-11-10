# ORDENAMIENTO POR SELECCIÓN (Selection Sort)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        indice_min = i #índice del menor valor encontrado

        #Recorre la lista buscando el valor mínimo
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        
        #intercambia el menor encontrado con el elemento actual
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
    return arr


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11]
    print("Original:", datos)
    print("Selection Sort:", selection_sort(datos.copy()))
