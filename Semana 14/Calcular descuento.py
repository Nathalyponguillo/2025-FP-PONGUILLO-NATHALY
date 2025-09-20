# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada: solo monto total
    monto1 = 300
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra 1:")
    print(f"  Monto total: ${monto1:.2f}")
    print(f"  Descuento aplicado (10% por defecto): ${descuento1:.2f}")
    print(f"  Total a pagar: ${total1:.2f}\n")

    # Segunda llamada: monto total y porcentaje personalizado
    monto2 = 85
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total2 = monto2 - descuento2
    print(f"Compra 2:")
    print(f"  Monto total: ${monto2:.2f}")
    print(f"  Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
    print(f"  Total a pagar: ${total2:.2f}")