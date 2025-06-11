'''
Se debe desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atrás en la historia de navegación.
1. Crea un diccionario llamado historiales que almacenará el historial de navegación para cada usuario. Las claves del
diccionario serán los nombres de usuario y los valores serán pilas de String.'''
'''2. Implementar una solución para el siguiente problema.
problema visitar sitio (inout historiales: Diccionario⟨seq⟨Char⟩, Pila[seq⟨Char⟩]⟩, in usuario: seq⟨Char⟩, in sitio: seq⟨Char⟩)
{
requiere: {Ninguno de los Strings de los parámetros es vacío}
asegura: {Si usuario es una de las claves de historiales@pre, entonces se agrega sitio a su pila de historiales@pre[usuario]}
asegura: {Si usuario no es una de las claves de historiales@pre, entonces historiales[usuario] es igual a la pila
que tiene solo el elemento sitio}
asegura: {No se modifica ningún otro historial salvo, si existe, el de usuario}
asegura: {Todos los pares clave-valor de historiales@pre están en historiales}
asegura: {Todos los pares clave-valor de historiales están en historiales@pre, salvo historiales[usuario] que
podría no existir en historiales@pre}
}'''

from queue import LifoQueue as Pila

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:

        if usuario in historiales.keys():
            historiales[usuario].put(sitio)

        else:
               historial_usuario: Pila[str] = Pila()
               historial_usuario.put(sitio)
               historiales[usuario] = historial_usuario