# Kendra Gutiérrez Vega, 2024

from pieza import Pieza
from coordenada import Coordenada

class Caballo(Pieza): # se crea la clase caballo

    def calcular_movimientos_posibles(self): # cálcula los movimientos posibles del caballo
        movimiento = []
        posicion_actual = self.get_posicion() # se obtiene la posición inicial

        movimientos_l = [ # lista de los movimientos del caballo
            (2, 1), (2, -1), # dos arriba, uno derecha o izquierda
            (-2, 1), (2, -1), # dos abajo, uno derecha o izquierda 
            (1, 2), (1, -2), # uno arriba, dos derecha o izquierda
            (-1, 2), (-1, -2) # uno abajo, dos derecha o izquierda
        ]

        for mov in movimientos_l: # revisa cada posible movimiento
            new_fila = posicion_actual.get_fila() + mov[0]
            new_columna = posicion_actual.get_columna() + mov[1]

        if 1 <= new_fila <= 8 and 1 <= new_columna <= 8: # verifica si el movimiento está dentro del tablero
            movimiento.append(Coordenada(new_fila, new_columna))
        
        return movimiento
