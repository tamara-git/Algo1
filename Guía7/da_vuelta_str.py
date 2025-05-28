''' problema da vuelta str (in s:seq⟨Char⟩) : seq⟨Char⟩ {
requiere: { T rue }
asegura: { |res| = |s| }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| − i − 1] }
}'''

def da_vuelta_str(lista:list[str]) ->list[str]:
    lista_reversa: list[str] = []
    for indice in range(len(lista)-1,-1,-1):
        lista_reversa = lista_reversa + [lista[indice]]
    return lista_reversa

print(da_vuelta_str(['T','A','M','I']))