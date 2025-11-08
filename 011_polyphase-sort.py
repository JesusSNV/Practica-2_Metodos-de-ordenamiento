# ORDENAMIENTO POLIFÁSICO (Polyphase Sort)

def ordenamiento_polifasico(arr):
    partes = [sorted(arr[i::3]) for i in range(3)]
    resultado = []
    indices = [0, 0, 0]

    while any(indices[i] < len(partes[i]) for i in range(3)):
        minimo = None
        pos = -1
        for i in range(3):
            if indices[i] < len(partes[i]):
                valor = partes[i][indices[i]]
                if minimo is None or valor < minimo:
                    minimo = valor
                    pos = i
        resultado.append(minimo)
        indices[pos] += 1

    return resultado


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Ordenamiento Polifásico:", ordenamiento_polifasico(datos.copy()))
