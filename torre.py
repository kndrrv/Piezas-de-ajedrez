# Kendra Gutiérrez, 2024

# se importan las clases Coordenada y Pieza
from pieza import Pieza
from coordenada import Coordenada

class Torre(Pieza): # se crea la clase Torre
    def calcular_movimientos_posibles(self): # cálcula los movimientos posibles para la torre
        movimiento = set() # se crea un set para que no se repitan los movimientos
        posicion_actual = self.get_posicion() # se obtiene la posición actual

        for columna in range(1, 9): # verifica los movimeintos de la torre (movimientos horizontales, misma fila todas la columnas)
            if columna != posicion_actual.columna: # no incluye la posición actual
                movimiento.add(Coordenada(posicion_actual.fila, columna))

        for fila in range(1, 9): # movimientos verticales, misma columna, todas las filas
            if fila != posicion_actual.fila: # no incluye la posición actual
                movimiento.add(Coordenada(fila, posicion_actual.columna))

        return movimiento