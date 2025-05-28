'''Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
sino que borra la vocal y concatena a continuaci´on.
problema sin vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { True }
asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}
Nota: Una subsecuencia de una cadena es una nueva secuencia'''

def sin_vocales(lista:list[str]) -> list[str]:
    lista = lista.copy()
    vocales = ['A','a','E','e','I','i','O','o','U','u']
    sin_vocales : list[str] = []
    for indice in range(len(lista)):
        if not(lista[indice] in vocales):
          sin_vocales = sin_vocales + [lista[indice]]
    return sin_vocales

print(sin_vocales(['t','a','m','a','r','a']))
