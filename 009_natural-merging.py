# ORDENAMIENTO POR MEZCLA NATURAL (Natural Merging)

def mezclar(a, b):
    """Mezcla dos listas ordenadas a y b y devuelve la lista resultante."""
    res = []
    i = j = 0
    #Compara los elementos de ambas listas
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    # anexar los restos
    if i < len(a):
        res.extend(a[i:])
    if j < len(b):
        res.extend(b[j:])
    return res

def mezcla_natural(arr):
    """Detecta corridas naturales (runs) y las mezcla hasta obtener la lista ordenada."""
    if not arr:
        return []

    #Detecta las sublistas ya ordenadas
    runs = []
    i = 0
    n = len(arr)
    while i < n:
        inicio = i
        i += 1
        while i < n and arr[i] >= arr[i-1]:
            i += 1
        runs.append(arr[inicio:i])

    #Mezcla las sublista de dos en dos hasta que quede una
    while len(runs) > 1:
        nuevas = []
        for k in range(0, len(runs), 2):
            if k + 1 < len(runs):
                nuevas.append(mezclar(runs[k], runs[k+1]))
            else:
                nuevas.append(runs[k]) #En caos de queda una sublista sin pareja
        runs = nuevas
    return runs[0]

if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Mezcla Natural:", mezcla_natural(datos.copy()))
