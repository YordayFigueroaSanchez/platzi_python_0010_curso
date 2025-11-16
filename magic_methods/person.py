class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

    def __repr__(self) -> str:
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __len__(self) -> int:
        return self.edad
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Persona):
            return self.nombre == other.nombre and self.edad == other.edad
        return False
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Persona):
            return self.edad < other.edad
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Persona):
            return Persona(f"{self.nombre} {other.nombre}", self.edad + other.edad)
        return NotImplemented

# Crear instancias de Persona
persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)
persona3 = Persona("Alice", 30)

# Usar los métodos mágicos
print(persona1)                # __str__

# Representación oficial
print(repr(persona1))          # __repr__

# Longitud (edad)
print(len(persona1))           # __len__

# Comparación de igualdad
print(persona1 == persona3)    # __eq__

# Comparación menor que
print(persona2 < persona1)     # __lt__

# Suma de personas
print(persona1 + persona2)    # __add__