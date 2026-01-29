# Algunos ejemplos sobre sets
lista = ["1",2,"3"] # son mutables
tupla = ("1",2,"3") # no son mutables
sets = {"1",2,"3"} # son mutables

set_from_lista = set(lista)
set_from_lista.add(4)
lista.append(4)
print(lista)
print(set_from_lista)

# Eliminar un elemento
set_from_lista.remove("3")
print(set_from_lista)

# Lista con duplicados
lista_con_duplicados = [1,2,2,1,3,7,4,9,3]
lista_sin_duplicados = []
for i in range(len(lista_con_duplicados)):
    if lista_con_duplicados[i] not in lista_sin_duplicados:
        lista_sin_duplicados.append(lista_con_duplicados[i])
print(lista_sin_duplicados)

# Lista sin duplicados con set
coleccion_sin_duplicados_set = set(lista_con_duplicados)
lista_sin_duplicados = list(coleccion_sin_duplicados_set)
print(coleccion_sin_duplicados_set)
print(lista_sin_duplicados)