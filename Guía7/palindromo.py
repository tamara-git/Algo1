'''Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
problema es palindroma (in s:seq⟨Char⟩) : Bool {
requiere: { T rue }
asegura: { (res = true) ↔ (s es igual a su reverso) }'''

def es_palindroma(lista:list[str]) -> bool:
    for indice in range(len(list)):
        if lista[indice] ==