'''problema reemplaza vocales (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = ' ') v
(¬ pertenece(<'a','e','i','o','u'>, s[i]) ∧ res[i] = s[i])) }
}
'''


def reemplaza_vocales(lista:list[str]) -> list[str]:
    lista_copia = lista.copy()
    vocales = ['A','a','E','e','I','i','O','o','U','u']
    reemplazo_vocal: list = []
    for indice in range (len(lista_copia)):
        if lista[indice] in vocales:
            lista[indice] = ''
        reemplazo_vocal = reemplazo_vocal + [lista[indice]]
    return reemplazo_vocal

print(reemplaza_vocales(['T','A','M','I']))
