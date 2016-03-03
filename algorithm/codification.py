from algorithm import sort as quick

__author__ = "Ragnarok"
__version__ = "0.0.1"
__doc__ = """

Código de Shannon-Fano

pasos para la encriptacion de Shannon-Fano
ordenar en orden decreciente
1º. Se toman los caracteres de más alta probabilidad y se obtienen dos subconjuntos, de tal modo que
 las sumas de las probabilidades de cada grupo sean, en la medida de lo posible, iguales.

2º. A todos los símbolos de la mitad superior se les agrega como primer símbolo del alfabeto de código
el 1 (o el cero) y a los inferiores el símbolo 0 (o el 1).

3º. Los dos subconjuntos se dividen a su vez en dos subgrupos con iguales probabilidades sumarias.
Se repite desde el primer paso.
"""


class ShannonFano:
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.shannon_fano = []
        self.order_probabilities = quick.QuickSort(self.probabilities, False).get_arr()
        self.cant_messages = len(self.probabilities)

        for i in range(self.cant_messages):
            self.shannon_fano.append("")

    @staticmethod
    def concat_zero():
        return lambda x: x + "0"

    @staticmethod
    def concat_one():
        return lambda x: x + "1"

    @staticmethod
    def center(arr):
        sum = 0
        for i in arr:
            sum += i
        return sum / 2

    @staticmethod
    def shannon(self, izq, der):
        # condiciones de parada
        if (izq - der) == 0:
            return
        elif (der - izq) == 1:  # si el arreglo en el que se esta trabajando tiene tamanno 1
            return
        elif (der - izq) == 2:  # si el arreglo en el que se esta trabajando tiene tamanno 2
            self.shannon_fano[izq] = self.concat_one()(self.shannon_fano[izq])
            self.shannon_fano[der - 1] = self.concat_zero()(self.shannon_fano[der - 1])
            return

        middle = self.center(self.order_probabilities[izq:der])
        current = 0
        separator = 0  # la posicion del que esta en el medio

        # determinar donde esta la mejor aproximacion
        for i in range(izq, der):
            current += self.order_probabilities[i]
            if current == middle:
                separator = i + 1
                break
            elif current > middle:
                before = current - self.order_probabilities[i]  # este es el anterior al pasarse del medio
                dif_before = abs(middle - before)
                dif_current = abs(middle - current)
                if dif_before <= dif_current:
                    # before is the divisor line
                    separator = i
                else:
                    # current is the divisor line
                    separator = i + 1
                break

        for i in range(izq, der):
            if i < separator:
                self.shannon_fano[i] = self.concat_one()(self.shannon_fano[i])
            else:
                self.shannon_fano[i] = self.concat_zero()(self.shannon_fano[i])

        self.shannon(self, izq, separator)
        self.shannon(self, separator, der)

    def get_message_encoded(self):
        if self.cant_messages == 1:
            self.shannon_fano[0] = "1"
        else:
            self.shannon(self, 0, der=self.cant_messages)
        return self.shannon_fano
