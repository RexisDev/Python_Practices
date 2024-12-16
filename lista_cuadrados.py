
# Lista de cuadrados
# Escribe una función que reciba una lista de números y devuelva otra lista con el cuadrado de cada número.
# Entrada: [1, 2, 3, 4]
# Salida esperada: [1, 4, 9, 16]


lista_numeros = [1, 2, 3, 4]

def lista_cuadrado(lista_numeros):
    
    lista_nueva = []
    
    for i in lista_numeros:
        lista_nueva.append(i**2)
    return lista_nueva

resultado = lista_cuadrado(lista_numeros)

print(resultado)