"""
1 - Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
2 - Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
3 - Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
4 - Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
bien cargados.
5 - Dada la siguiente lista de ingresos horarios:
[ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
a) Calcular el promedio de ingresos/hora del 20% que más gana.
b) Calcular el promedio de ingresos/hora de todos los respondentes.
c) Buscar cuál es el valor que más se repite.
d) Calcular la media geométrica
6- Suponiendo que tenemos dos listas en las cuales la posición es la misma en ambas para
cada respondente:
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = [“Juan”, “Matias”, “Carla”, “Susana”, “Olivia”, “Carlos”, “Daniel”, “Jimena”,
“Mariela”, “Ignacio”]
a) Devolver el nombre del respondiente más jóven y del más grande.
b) Genere dos nuevos listado por sexo y calcule la media etaria para varones y mujeres
c) Utilizando continue, calcule la media etaria para mayores de 40 años
"""
"""#1
nombre = input("ingrese su nobre")
apellido = input("ingrese su apellido")
#2
salario_mensual = int(input("ingrese su salario mensual"))
#3
horas_trabajadas = int(input("ingrese las horas trabajadas"))
while horas_trabajadas < 0 and horas_trabajadas < 121:
    horas_trabajadas = int(input("ingrese correctamente las horas trabajadas"))
#4
ingreso_horario = salario_mensual / horas_trabajadas
#5
horarios = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
#a
porcentaje_20 = int(len(horarios)*0.2)
#NO SALEEE
"""


#6
lista_edad = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena","Mariela", "Ignacio"]

edad_mas_grande = float('-inf')
edad_mas_baja = float('inf')

for index in range(len(lista_edad)):

    if lista_edad[index] > edad_mas_grande:
        edad_mas_grande = lista_edad[index]
    elif lista_edad[index] < edad_mas_baja:
        edad_mas_baja = lista_edad[index]    

print(edad_mas_grande)
print(edad_mas_baja)

