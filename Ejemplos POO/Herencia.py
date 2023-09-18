class Operacion:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def realizar_operacion(self):
        pass

class Suma(Operacion):
    def realizar_operacion(self):
        return self.operando1 + self.operando2

# Creamos una instancia de la subclase Suma
suma = Suma(5, 3)
resultado_suma = suma.realizar_operacion()

print(f"El resultado de la suma es: {resultado_suma}")
