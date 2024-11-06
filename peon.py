# Kendra Gutiérrez Vega, 2024

# se importan las clases Pieza y Coordenada
from pieza import Pieza
from coordenada import Coordenada

class Peon(Pieza): # se crea la clase Peón
    def calcular_movimientos_posibles(self): # cálcula los movimientos posibles del peón
        movimiento = []
        posicion_actual = self.get_posicion() # se obtiene la posición actual

        if self.get_color() == "blanco": # vamos a determinar si el peón sube o baja según su color
            if posicion_actual == 2: # primera jugada del peón blanco
                movimiento.append(Coordenada(3, posicion_actual.get_columna())) # puede moverse una o dos casillas hacia delante
                movimiento.append(Coordenada(4, posicion_actual.get_columna()))
            elif posicion_actual.get_fila() < 8: # cualquier otra jugada
                movimiento.append(Coordenada(posicion_actual.get_fila() + 1, posicion_actual.get_columna())) # solo puede moverse una casilla hacia delante
        else:
            if posicion_actual.get_fila() == 7: # primera jugada del peón negro
                movimiento.append(Coordenada(6, posicion_actual.get_columna())) # puede moverse una o dos casillas hacia delante
                movimiento.append(Coordenada(5, posicion_actual.get_columna()))
            elif posicion_actual.get_fila() > 1: # cualquier otra
                movimiento.append(Coordenada(posicion_actual.get_fila() -1, posicion_actual.get_columna())) # solo puede moverse una casilla hacia delante
        return movimiento