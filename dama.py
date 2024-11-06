from pieza import Pieza
from coordenada import Coordenada

class Dama(Pieza): # se crea la clase dama

    def calcular_movimientos_posibles(self):
        movimiento = []
        posicion_actual = self.get_posicion()

        # movimientos como torre, horizontal y vertical
        for columna in range(1, 9): # horizontal
            if columna != posicion_actual.get_columna():
                movimiento.append(Coordenada(posicion_actual.get_fila(), columna))
        
        for fila in range(1, 9): # vertical
            if fila != posicion_actual.get_fila():
                movimiento.append(Coordenada(fila, posicion_actual.get_columna()))

        # movimientos como alfil, diagonales
        for i in range(1, 8):
            direcciones = [
                (i, i),    # Superior derecha
                (i, -i),   # Superior izquierda
                (-i, i),   # Inferior derecha
                (-i, -i)   # Inferior izquierda
            ]

        for dir in direcciones:
            new_fila = posicion_actual.get_fila() + dir[0]
            new_columna = posicion_actual.get_columna() + dir[1]

            if 1 <= new_fila <= 8 and 1 <= new_columna <= 8: # verifica si el moviemiento está dentro del tablero
                    movimiento.append(Coordenada(new_fila, new_columna))

        return movimiento