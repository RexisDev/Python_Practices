
# Tuplas de índices y valores
# Escribe una función que tome una lista como argumento y devuelva una lista de tuplas donde cada tupla contenga el índice y el valor correspondiente.
# Entrada: ['a', 'b', 'c']
# Salida esperada: [(0, 'a'), (1, 'b'), (2, 'c')]

lista_arg = ['a', 'b', 'c']


def indice_valor(lista_arg):
    
    mi_tuple_list = []
    
    for i in lista_arg:

        mi_tuple_list.append(tuple(f"{lista_arg.index(i)}{i}"))
        
    return mi_tuple_list
    
resultado = indice_valor(lista_arg)

print(resultado)