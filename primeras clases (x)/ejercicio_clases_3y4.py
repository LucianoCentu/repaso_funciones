#1
def mostrar_numero(numero):
    print(f"El numero es: {numero}")

num = int(input("Ingrese su numero: "))
mostrar_numero(num)


#2
def definir_par_inpar(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False

num2 = int(input("Ingrese su numero: "))
definir_par(num2)

#3
def mostrar_numero_desde_hasta(numero, desde, hasta):
    if desde <= numero <= hasta:
        print(f"El numero {numero} esta dentro del rango [{desde}, {hasta}]")
    else:
        print(f"El numero {numero} esta fuera del rango [{desde}, {hasta}]")

num3 = int(input("Ingrese su numero: "))
desde_num = int(input("Ingrese su limite inferior: "))
hasta_num = int(input("Ingrese su limite superior: "))

mostrar_numero_desde_hasta(num3, desde_num, hasta_num)

#4
def restar(numero_1: int, numero_2: int)-> int:
    resta = numer1 - numer2
    return resta

numer1 = int(input("Ingrese su numero 1: "))
numer2 = int(input("Ingrese su numero 2: "))

restar()

def restar2()-> int:
    return 20 - 5

restar2()

def restar3(numero_1:int , numero_2: int):
    print(numero_1 - numero_2) 

restar3()

def restar4():
    print(20 - 5)

restar4()

#5
def realizar_descuento(valor):
    return valor * 0.95

numero1 = int(input("Ingrese un valor entre 10 y 100: "))
if 10 <= numero1 <= 100:
    numero_con_descuento = realizar_descuento(numero1)
    print(f"El valor con el descuento es: {numero_con_descuento}")
else:
    print("El numero no esta en el rango.")

#6
def asignar_numeros(a, b, operacion):
    if operacion == 's':
        return a + b
    elif operacion == 'r':
        return a - b
    else:
        return None

numero1 = int(input("Ingrese un valor entre 10 y 100: "))
numero2 = int(input("Ingrese otro valor entre 10 y 100: "))
if 10 <= numero1 <= 100 and 10 <= numero2 <= 100:
    operacion = input("Ingrese 's' para sumar o 'r' para restar: ")
    if operacion in ['s', 'r']:
        resultado = asignar_numeros(numero1, numero2, operacion)
        print(f"El resultado de la operación es: {resultado}")
    else:
        print("Operación no valida.")
else:
    print("Uno o ambos numeros no están en el rango.")

#7
def calcular_impuesto_nacional(valor_ventas_nacionales, iva = 21):
    #calcula el valor neto de ventas nacionales sin IVA.
    return valor_ventas_nacionales / (1 + (iva / 100))

def calcular_impuesto_exportaciones(valor_exportaciones, retenciones = 15):
    #calcula el valor de exportaciones despues de retenciones.
    return valor_exportaciones * (1 - (retenciones / 100))

def calculo_impuestos_total(valor_exportaciones, valor_ventas_nacionales, iva=21, retenciones=15):
    #calcula el total de impuestos sumando ventas nacionales y exportaciones.
    total_nacional = calcular_impuesto_nacional(valor_ventas_nacionales, iva)
    total_exportaciones = calcular_impuesto_exportaciones(valor_exportaciones, retenciones)
    return total_nacional + total_exportaciones

#8
def calcular_salario(horas_trabajadas, anios_antiguedad):
    #calcula el salario segun horas trabajadas y antigüedad.
    salario_base = horas_trabajadas * 10
    bono_antiguedad = salario_base * (0.03 * anios_antiguedad)
    return salario_base + bono_antiguedad

def calcular_productividad(artefactos_producidos, horas_trabajadas):
    #calcula la productividad como artefactos producidos por hora.
    if horas_trabajadas == 0:
        return 0
    return artefactos_producidos / horas_trabajadas

def reporte_empleado(nombre, edad, horas_trabajadas, anios_antiguedad, artefactos_producidos):
    #Genera un reporte con la información del empleado.
    salario = calcular_salario(horas_trabajadas, anios_antiguedad)
    productividad = calcular_productividad(artefactos_producidos, horas_trabajadas)
    return (f"Nombre: {nombre}\nEdad: {edad}\nSalario: {salario}\nProductividad: {productividad}")