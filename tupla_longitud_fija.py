# Tuplas de longitud fija
# Escribe una función que reciba una lista de palabras y devuelva una lista de tuplas. Cada tupla debe contener una palabra y su longitud.
# Entrada: ['Python', 'Code', 'List']
# Salida esperada: [('Python', 6), ('Code', 4), ('List', 4)]

lista_palabras = ['Python', 'Code', 'List']

def elem_tupla(lista_palabras):
    
    tuple_list = []
    
    for i in lista_palabras:
        
        tuple(tuple_list.append(i) + tuple_list.append(len(i)))
        
    print(tuple_list)

resultado = elem_tupla(lista_palabras)

print(resultado)