
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
    reporte = (f"Nombre: {nombre}\nEdad: {edad}\nSalario: {salario}\nProductividad: {productividad}")
    return reporte 
