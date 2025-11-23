def mi_funcion():
    print("Hola mundo")

# crear funcion saludos y pasarle a quien saludo
def saludo(nombre):
    print("Hola", nombre)

# crear funcion despedida y pasarle a quien despedi. agregar de donde es y colocar valor por defecto
def despedida(nombre, lugar="la casa"):
    print("Adios", nombre, "desde", lugar)

saludo("Juan")
despedida("Juan")
despedida("Juan", "la playa")