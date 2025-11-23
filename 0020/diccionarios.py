# Diccionarios

auto = {
    "marca": "toyota",
    "modelo": "corolla",
    "anio": 2020
}
print(auto)
print(type(auto))
print(len(auto))
print(auto["marca"])

# obtener la keys
print(auto.keys())

# obtener los values
print(auto.values())

# obtener los items
print(auto.items())

# agregar un item
auto["color"] = "rojo"
print(auto)

# modificar un item
auto["anio"] = 2021
print(auto)

# eliminar un item
auto.pop("color")
print(auto)

# eliminar el ultimo item
auto.popitem()
print(auto)

# copiar un diccionario
auto2 = auto.copy()
print(auto2)

# eliminar todos los items
auto.clear()
print(auto)

# eliminar el diccionario
# del auto

# usar update para cambiar info en el diccionario
auto.update({"anio": 2022})
print(auto)

# usar update para agregar mas de un item
auto.update({"color": "rojo", "anio": 2023})
print(auto)

# recorrer el diccionario
for key, value in auto.items():
    print(key, value)

# recorrer el diccionario con keys
for key in auto.keys():
    print(key)

# recorrer el diccionario con values
for value in auto.values():
    print(value)

# diccionarios anidados
familia = {
    "padre": {
        "nombre": "juan",
        "edad": 40
    },
    "madre": {
        "nombre": "ana",
        "edad": 35
    },
    "hijo": {
        "nombre": "pedro",
        "edad": 10
    }
}
print(familia)
print(familia["padre"]["nombre"])