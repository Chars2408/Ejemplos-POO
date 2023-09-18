class CalculadoraSueldo:
    def __init__(self):
        self.sueldo_base = 0
        self.ventas_realizadas = 0

    def solicitar_datos(self):
        self.sueldo_base = float(input("Ingrese el sueldo base: "))
        self.ventas_realizadas = float(input("Ingrese el valor de ventas realizadas: "))

    def calcular_comision(self):
        return 0.10 * self.ventas_realizadas

    def calcular_igss(self):
        return 0.0483 * self.sueldo_base

    def calcular_ahorro(self):
        return 0.07 * (self.sueldo_base + self.calcular_comision())

    def calcular_total_ganado(self):
        return self.sueldo_base + self.calcular_comision() + self.calcular_ahorro()

    def calcular_total_descuentos(self):
        return self.calcular_ahorro() + self.calcular_igss()

    def calcular_sueldo_liquido(self):
        return self.calcular_total_ganado() - self.calcular_total_descuentos()


calculadora = CalculadoraSueldo()
calculadora.solicitar_datos()

comision = calculadora.calcular_comision()
igss = calculadora.calcular_igss()
ahorro = calculadora.calcular_ahorro()
total_ganado = calculadora.calcular_total_ganado()
total_descuentos = calculadora.calcular_total_descuentos()
sueldo_liquido = calculadora.calcular_sueldo_liquido()

print(f'a. Comisión por ventas: {comision}')
print(f'b. IGSS: {igss}')
print(f'c. Ahorro: {ahorro}')
print(f'd. Total ganado: {total_ganado}')
print(f'e. Total descuentos: {total_descuentos}')
print(f'f. Sueldo líquido: {sueldo_liquido}')
