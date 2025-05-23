'''Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
problema es palindroma (in s:seq⟨Char⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (s es igual a su reverso) }'''

def reverso(lista:list[str]) -> list[str]:
    reverso : list = []
    for indice in range(len(lista)-1,-1,-1):
        reverso.append(lista[indice])
    return reverso

print(reverso(['h','o','l','a']))

def es_palindromo(lista:list[str]) -> bool:
        if lista == reverso(lista):
            return True
        else:
            return False
        
print(es_palindromo(['s','o','m','e','t','e','m','o','s']))