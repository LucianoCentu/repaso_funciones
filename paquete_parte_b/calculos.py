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
    resultado_ventas = total_nacional + total_exportaciones
    return resultado_ventas