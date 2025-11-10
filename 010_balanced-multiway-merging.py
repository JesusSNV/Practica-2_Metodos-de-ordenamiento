# ORDENAMIENTO POR MEZCLA BALANCEADA MULTIVÍA (Balanced Multiway Merging)

def mezcla_balanceada_multivia(lista, vias=3):
    #Divide la lista original en 3 vías
    runs = [sorted(lista[i::vias]) for i in range(vias)]
    
    #Índices para seguir el progreso en cada vía
    resultado = []
    indices = [0] * vias

    #Mientras haya elementos en alguna vía
    while any(indices[i] < len(runs[i]) for i in range(vias)):
        minimo = None
        pos = -1
        #Busca el menor valor 
        for i in range(vias):
            if indices[i] < len(runs[i]):
                valor = runs[i][indices[i]]
                if minimo is None or valor < minimo:
                    minimo = valor
                    pos = i
        #Añade el menor valor al resultado y avanza al sig. índice
        resultado.append(minimo)
        indices[pos] += 1
    return resultado


if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11, 90, 34]
    print("Original:", datos)
    print("Mezcla Balanceada Multivía:", mezcla_balanceada_multivia(datos.copy()))