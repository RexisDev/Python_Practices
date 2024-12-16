# Intercambia elementos
# Crea una función que reciba una tupla con dos elementos y devuelva una nueva tupla con los elementos intercambiados.
# Entrada: (1, 'Python')
# Salida esperada: ('Python', 1)

mi_tupla = (1, 'Python')

def intercambio(mi_tupla):
    
    return mi_tupla[1], mi_tupla[0]
    
resultado = intercambio(mi_tupla)

print(resultado)