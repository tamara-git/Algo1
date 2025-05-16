#problema es_nombre_largo (in nombre: String) : Bool {
#requiere: { True }
#asegura: {(res = true) ↔ (3 ≤ |nombre| ≤ 8)}
#}

def es_nombre_largo (nombre:str) -> bool:
    return (len(nombre) >= 3 and len(nombre) <= 8) 
print (es_nombre_largo("Laura"))