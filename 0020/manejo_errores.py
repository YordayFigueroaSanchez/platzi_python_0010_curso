# tratamientos de errores

# division por zero
try:
    1 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print("Ocurrio un error:", e)

# imprimir variable no definida
try:
    print(x)
except NameError:
    print("La variable no esta definida")
except Exception as e:
    print("Ocurrio un error:", e)
finally:
    print("Fin del programa")