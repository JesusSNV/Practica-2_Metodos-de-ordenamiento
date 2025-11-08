# DISTRIBUCIÓN DE SERIES INICIALES (Distribution of Initial Runs)

def distribucion_series_iniciales(arr):
    series = []
    i = 0
    while i < len(arr):
        inicio = i
        while i + 1 < len(arr) and arr[i] <= arr[i + 1]:
            i += 1
        fin = i + 1
        series.append(arr[inicio:fin])
        i = fin
    series = [sorted(s) for s in series]
    resultado = []
    for s in series:
        resultado.extend(s)
    return sorted(resultado)


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Distribución de Series Iniciales:", distribucion_series_iniciales(datos.copy()))
