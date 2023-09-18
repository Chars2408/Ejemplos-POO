class ProcesadorTextos:
    def __init__(self):
        self.textos = []

    def solicitar_textos(self):
        for i in range(3):
            texto = input(f'Ingrese el texto {i+1}: ')
            self.textos.append(texto)

    def promedio_longitudes(self):
        total_longitudes = sum(len(texto) for texto in self.textos)
        return total_longitudes / len(self.textos)

    def concatenar_textos(self):
        texto_concatenado = ''.join(self.textos)
        largo = len(texto_concatenado)
        if largo > 15:
            return f'La concatenación tiene más de 15 caracteres ({largo} caracteres en total).'
        elif largo < 15:
            return f'La concatenación tiene menos de 15 caracteres ({largo} caracteres en total).'
        else:
            return f'La concatenación tiene exactamente 15 caracteres ({largo} caracteres en total).'

    def texto_con_mas_caracteres(self):
        texto_mas_largo = max(self.textos, key=len)
        return f'El texto con más caracteres es: "{texto_mas_largo}"'

    def caracteres_numericos(self):
        texto_concatenado = ''.join(self.textos)
        cantidad_numericos = sum(caracter.isdigit() for caracter in texto_concatenado)
        return f'Hay {cantidad_numericos} caracteres numéricos en la concatenación de los textos.'


procesador = ProcesadorTextos()
procesador.solicitar_textos()

print(f'a. Promedio de longitudes: {procesador.promedio_longitudes()}')
print(f'b. {procesador.concatenar_textos()}')
print(f'c. {procesador.texto_con_mas_caracteres()}')
print(f'd. {procesador.caracteres_numericos()}')
