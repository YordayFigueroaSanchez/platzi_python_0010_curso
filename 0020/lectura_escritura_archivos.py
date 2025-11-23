# lectura y escritura de archivos de texto

# tipos de apertura
# R: lectura
# W: escritura
# X: crea el archivo

# abrir archivo
try:
    with open("0020/archivo.txt", "r", encoding="utf-8") as archivo:
        print(archivo.readline())
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    print("Fin del programa")

# escribir en archivo
try:
    with open("0020/archivo.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Hola mundo")
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    print("Fin del programa")

# append en archivo
try:
    with open("0020/archivo.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\nHola mundo")
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    print("Fin del programa")


# abrir archivo, crearlo en caso de no encontrarlo
try:
    with open("0020/archivo2.txt", "r", encoding="utf-8") as archivo:
        print(archivo.readline())
except FileNotFoundError:
    print("El archivo no existe")
    open("0020/archivo2.txt", "w", encoding="utf-8").close()
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    print("Fin del programa")