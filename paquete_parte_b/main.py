from calculos import calculo_impuestos_total
from rrhh import reporte_empleado
#7
def main():
    valor_exportaciones = float(input("Ingrese el valor de las exportacion: "))
    valor_ventas_nacionales = float(input("Ingrese el valor (IVA incluido) de las ventas nacionales: "))
    resultado = calculo_impuestos_total(valor_exportaciones, valor_ventas_nacionales)
    print(f"El valor total de las ventas con impuestos y retenciones es de {resultado}")
if __name__ == "__main__":
    main()

#8
nombre = input("Ingrese el nombre del empleado: ")
edad = int(input("Ingrese la edad del empleado: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
anios_antiguedad = int(input("Ingrese los años de antigüedad: "))
artefactos_producidos = int(input("Ingrese la cantidad de artefactos producidos: "))
reporte = reporte_empleado(nombre, edad, horas_trabajadas, anios_antiguedad, artefactos_producidos)
print("\nReporte del empleado:")
print(reporte)
