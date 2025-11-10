# ORDENAMIENTO RADIX (Radix Sort)

def counting_sort_para_radix(arr, exp):
    n = len(arr)
    salida = [0] * n    #Lista de salida ordenada parcialmente
    conteo = [0] * 10   #Para dígitos de 0 al 9

    #Cuenta las ocurrencias de cada dígito
    for i in range(n):
        indice = (arr[i] // exp) % 10
        conteo[indice] += 1

    #Acumula posiciones
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    #Construye la lista de salida ordenada
    i = n - 1
    while i >= 0:
        indice = (arr[i] // exp) % 10
        salida[conteo[indice] - 1] = arr[i]
        conteo[indice] -= 1
        i -= 1

    #Copia la salida al arreglo original
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    #Encuentra el número máximo para saber cuantos dígitos tiene
    max_val = max(arr)
    exp = 1
    #Counting sort para cada dígito
    while max_val // exp > 0:
        counting_sort_para_radix(arr, exp)
        exp *= 10
    return arr


if __name__ == "__main__":
    datos = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original:", datos)
    print("Radix Sort:", radix_sort(datos.copy()))
