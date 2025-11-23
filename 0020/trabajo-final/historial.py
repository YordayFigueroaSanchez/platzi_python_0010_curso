ARCHIVO_PEDIDOS = "0020/trabajo-final/pedidos.txt"


def mostrar_pedidos():
    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos):
                    print(f"{i + 1}. {pedido}")
            else:
                print("No hay pedidos")
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print("Ocurrio un error:", e)
    finally:
        print("Fin del programa")
