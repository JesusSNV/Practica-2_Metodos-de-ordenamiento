# ORDENAMIENTO DE ÁRBOL (Tree Sort)

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izq = insertar(nodo.izq, valor)
    else:
        nodo.der = insertar(nodo.der, valor)
    return nodo

def recorrido_inorden(nodo, resultado):
    if nodo is not None:
        recorrido_inorden(nodo.izq, resultado)
        resultado.append(nodo.valor)
        recorrido_inorden(nodo.der, resultado)

def tree_sort(arr):
    if not arr:
        return []
    raiz = Nodo(arr[0])
    for i in range(1, len(arr)):
        insertar(raiz, arr[i])
    resultado = []
    recorrido_inorden(raiz, resultado)
    return resultado


if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", datos)
    print("Tree Sort:", tree_sort(datos.copy()))
