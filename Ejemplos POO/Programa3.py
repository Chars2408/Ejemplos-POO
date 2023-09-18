class CalculadoraNumeros:
    def __init__(self):
        self.numero = 0

    def solicitar_numero(self):
        self.numero = int(input("Ingrese un número entero positivo: "))
        if self.numero < 0:
            print("El número debe ser positivo. Intenta nuevamente.")
            self.solicitar_numero()

    def calcular_factorial(self):
        factorial = 1
        for i in range(1, self.numero + 1):
            factorial *= i
        return factorial

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False
        return True

    def es_perfecto(self):
        suma = 0
        for i in range(1, self.numero):
            if self.numero % i == 0:
                suma += i
        return suma == self.numero

    def convertir_a_binario(self):
        return bin(self.numero)[2:]


calculadora = CalculadoraNumeros()
calculadora.solicitar_numero()

factorial = calculadora.calcular_factorial()
es_primo = calculadora.es_primo()
es_perfecto = calculadora.es_perfecto()
binario = calculadora.convertir_a_binario()

print(f'a. Factorial: {factorial}')
print(f'b. Es primo: {es_primo}')
print(f'c. Es perfecto: {es_perfecto}')
print(f'd. Binario: {binario}')
