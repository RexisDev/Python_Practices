
# Crea una función que tome una lista de números como argumento y devuelva una nueva lista con solo los números pares.
# Entrada: [1, 2, 3, 4, 5, 6]
# Salida esperada: [2, 4, 6]

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numeros_pares(lista_numeros):
    
    lista_nueva = []
    
    for i in lista_numeros:
        if i % 2 == 0:
            lista_nueva.append(i)
    return lista_nueva
            
resultado = numeros_pares(lista_numeros)

print(resultado)