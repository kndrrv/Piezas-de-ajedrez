# Kendra Gutiérrez Vega, 2024

from pieza import Pieza
from coordenada import Coordenada

class Alfil(Pieza): # se crea la clase alfil

    def calcular_movimientos_posibles(self): # cálcula los posibles movimientos
        movimiento = set() # se crea un set para evitar movimientos repetidos
        posicion_actual = self.get_posicion # se obtiene la posición actual

        # revisa las cuatro direcciones en diagonal
        for i in range(1, 8): # puede moverse hasta 7 casillas en cada dirección
            # diagonal superior derecha
            new_fila = posicion_actual.fila + i 
            new_columna = posicion_actual.columna + i
            if 1 <= new_fila <= 8 and 1 <= new_columna <= 8:
                movimiento.add(Coordenada(new_fila, new_columna))

            # diagonal superior izquierda
            new_columna = posicion_actual.columna - i
            if 1 <= new_fila <= 8 and 1 <= new_columna <= 8:
                movimiento.add(Coordenada(new_fila, new_columna))
            
            # diagonal inferior derecha
            new_fila = posicion_actual.fila - i 
            new_columna = posicion_actual.columna + i
            if 1 <= new_fila <= 8 and 1 <= new_columna <= 8:
                movimiento.add(Coordenada(new_fila, new_columna))

            # diagonal inferior izquierda
            new_columna = posicion_actual.columna - i
            if 1 <= new_fila <= 8 and 1 <= new_columna <= 8:
                movimiento.add(Coordenada(new_fila, new_columna))

        return movimiento