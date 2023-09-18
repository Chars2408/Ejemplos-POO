import math

def obtener_valores():
    try:
        valor1 = int(input("Ingresa el primer valor entero: "))
        valor2 = int(input("Ingresa el segundo valor entero: "))
        return valor1, valor2
    except ValueError:
        print("Error: Ingresa valores enteros.")

def suma(val1, val2):
    return val1 + val2

def multiplicacion(val1, val2):
    return val1 * val2

def promedio(val1, val2):
    return (val1 + val2) / 2

def mayor_menor_igual(val1, val2):
    if val1 > val2:
        return f"{val1} es mayor y {val2} es menor."
    elif val2 > val1:
        return f"{val2} es mayor y {val1} es menor."
    else:
        return f"{val1} y {val2} son iguales."

def par_o_impar_multiplicacion(val1, val2):
    resultado_multiplicacion = val1 * val2
    if resultado_multiplicacion % 2 == 0:
        return "La multiplicación es par."
    else:
        return "La multiplicación es impar."

def raiz_cuadrada_suma(val1, val2):
    resultado_suma = val1 + val2
    return math.sqrt(resultado_suma)

if __name__ == "__main__":
    valor1, valor2 = obtener_valores()

    print(f"a. Suma: {suma(valor1, valor2)}")
    print(f"b. Multiplicación: {multiplicacion(valor1, valor2)}")
    print(f"c. Promedio: {promedio(valor1, valor2)}")
    print(f"d. {mayor_menor_igual(valor1, valor2)}")
    print(f"e. {par_o_impar_multiplicacion(valor1, valor2)}")
    print(f"f. Raíz cuadrada de la suma: {raiz_cuadrada_suma(valor1, valor2)}")


    
