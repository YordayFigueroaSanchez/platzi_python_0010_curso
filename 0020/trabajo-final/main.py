from menu import mostrar_menu   
from pedidos import pedir_cafe
from historial import mostrar_pedidos

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            mostrar_pedidos()
        elif opcion == "3":
            print("Muchas gracias, hasta pronto")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    main()
        