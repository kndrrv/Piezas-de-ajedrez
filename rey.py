# Kendra Gutiérrez Vega, 2024

from pieza import Pieza
from coordenada import Coordenada

class Rey(Pieza): # se crea la clase rey

    def calcular_movimientos_posibles(self): # cálcula los posibles movimientos
        movimiento = []
        posicion_actual = self.get_posicion() # obtiene la posición actual

        # el rey puede moverse a una casilla en cualquier dirección
        for fila_diff in [-1, 0, 1]: # arriba, mismo nivel, abajo
            for columna_diff in [-1, 0, 1]: # izquierda, mismo lugar, derecha
                if fila_diff == 0 and columna_diff == 0: # salta la posición actual
                    continue

                new_fila = posicion_actual.get_fila() + fila_diff
                new_columna = posicion_actual.get_columna() + columna_diff

                if 1 <= new_fila <= 8 and 1 <= new_columna <= 8: # verifica si el moviemiento está dentro del tablero
                    movimiento.append(Coordenada(new_fila, new_columna))

        return movimiento
