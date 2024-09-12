#For de 0 a 4 usando range
"""for numero in range (5):
    print(f"El mumero es {numero}")

#cortar
for numero in range (5):
    print(f"El mumero es {numero}")
    if numero == 3:
        break

#numeros pares
for numero in range (20):
    if (numero % 2) == 1:
        continue
    else:
        print(f"El mumero es {numero}")


#string
for letra in "perro":
    if letra == "r":
        continue
    else:
        print(letra)


#iter == iterable

palabra = "Hola Mundo"

if iter(palabra):
    print("se puede iterar")"""

"""if iter(True):
    print("se puede iterar")
"""

#funcion LEN

frase = "Soy una frase"

"""print(len(frase))
print(len(range(18)))

lista = [1, "perro", 1.33]

print(len(lista))
print(type(lista))

for objeto in lista:
    print(objeto)"""

for posicion in range(1, len(frase), 2):
    print(frase[posicion])
