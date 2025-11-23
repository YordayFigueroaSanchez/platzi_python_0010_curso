ARCHIVO_PEDIDOS = "0020/trabajo-final/pedidos.txt"

def pedir_cafe():
    print("\n Que cafe desea pedir?")
    print("1. Express")
    print("2. Capuchino")
    print("3. Mocha")
    print("4. Americano")
    print("5. Latte")
    
    cafes = {
        "1": "Express",
        "2": "Capuchino",
        "3": "Mocha",
        "4": "Americano",
        "5": "Latte"
    }

    opcion = input("Ingrese una opcion: ")
    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Pediste", cafe_elegido)
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write("Pediste " + cafe_elegido + "\n")
    else:
        print("Opcion no valida")
