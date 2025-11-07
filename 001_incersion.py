# ORDENAMIENTO POR SELECCIÓN (Selection Sort)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        indice_min = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_min]:
                indice_min = j
        arr[i], arr[indice_min] = arr[indice_min], arr[i]
    return arr


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11]
    print("Original:", datos)
    print("Selection Sort:", selection_sort(datos.copy()))
