'''. problema divide a todos (in s:seq⟨Z⟩, in e: Z) : Bool {
requiere: { e ̸= 0 }
asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0) }
}'''

def divide_a_todos(lista:list[int],numero:int) -> bool:
    for elemento in lista:
        if not(elemento % numero == 0):
            return False 
    else:
        return True

print(divide_a_todos([2,3,4,6,8],2))
print(divide_a_todos([6,9,90],3))