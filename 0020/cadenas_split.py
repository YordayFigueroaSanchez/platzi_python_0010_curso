texto = "Este es un texto"

print(texto[0:4])

# desde el inicio hasta el 4to
print(texto[:4])

# desde el 2 hasta el final
print(texto[2:])

# usar los negativos - desde el inicio hasta el segundo desde el final
print(texto[:-2])

curso =  "Este curso es de Javascript"
print(curso.replace('Javascript','Python'))

textoDividido = texto.split(' ')
print(textoDividido)

texto2 = 'Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras'
print(texto2.lower())
print('mayusculas'.lower() in texto2.lower())