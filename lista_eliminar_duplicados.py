
# Elimina duplicados
# Dada una lista, escribe una función que elimine los valores duplicados manteniendo el orden original.
# Entrada: [1, 2, 2, 3, 4, 4, 5]
# Salida esperada: [1, 2, 3, 4, 5]

lista_numeros = [1, 2, 2, 3, 4, 4, 5]

def elim_duplicados(lista_numeros):
    
    lista_nueva = []
    
    for i in lista_numeros:
        if i in lista_nueva:
            pass
        else:
            lista_nueva.append(i)        
    return lista_nueva

resultado = elim_duplicados(lista_numeros)

print(resultado)