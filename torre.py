# Kendra Gutiérrez, 2024

# se importan las clases Coordenada y Pieza
from pieza import Pieza
from coordenada import Coordenada

class Torre(Pieza): # se crea la clase Torre
    def calcular_movimientos_posibles(self): # cálcula los movimientos posibles para la torre
        movimiento = []
        posicion_actual = self.get_posicion() # se obtiene la posición actual

        for columna in range(1, 9): # verifica los movimeintos de la torre (movimientos horizontales, misma fila todas la columnas)
            if columna != posicion_actual.get_columna(): # no incluye la posición actual
                movimiento.append(Coordenada(posicion_actual.get_fila(), columna))

        for fila in range(1, 9): # movimientos verticales, misma columna, todas las filas
            if fila != posicion_actual.get_fila(): # no incluye la posición actual
                movimiento.append(Coordenada(fila, posicion_actual.get_columna()))

        return movimiento