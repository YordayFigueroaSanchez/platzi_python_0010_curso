try:
    # print(0/0)
    age = 10
    if (age < 18):
        raise Exception("No se permiten menores")
    assert 1 != 1, '1 no es igual a 1'
except ZeroDivisionError:
    print("No se puede dividir por cero")
except AssertionError:
    print("1 no es igual a 1")
except Exception as e:
    print(e)
print('continuamos...')

