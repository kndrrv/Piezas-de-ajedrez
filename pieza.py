class Pieza: # se crea la clase Pieza
    def __init__(self, color, posicion): # se crea el constructor y se recibe como parámetros self, color y posicion
        self.__color = color # se agregan los atributos utilizando self para poder acceder a ellos y se utiliza __ volverlo privado
        self.__posicion = posicion # evitando que se puedan modificar o acceder a ellos de forma directa fuera de la clase
    
    def __eq__(self, otro_objeto): # método para comparar si dos piezas son iguales
        if not isinstance(otro_objeto, Pieza): # verifica que el objeto esté en la misma instancia de la clase
            return False
        return self.color == otro_objeto.color and \
            self.__posicion == otro_objeto.__posicion # compara el color y la posición de la pieza

    # getter y setter de color
    def get_color(self): # se utiliza el método getter para acceder al atributo privado __color
        return self.__color

    def set_color(self, new_color): # se utiliza el método getter para para modificar el atributo __color
        self.__color = new_color

    # getter y setter de posición
    def get_posicion(self): # el método getter nos ayuda a acceder al atributo privado __posicion
        return+ self.__posicion

    def set_posicion(self, new_posicion): # el método getter nos ayuda a modificar el atributo privado __posicion
        self.__posicion = new_posicion

    def __str__(self):# método para representar la pieza como un string, indicando su nombe, color y posición
        return f"{self.__class__.__name__} {self.__color} en {self.__posicion}"

    def mover(self, casilla_destino): # este método verifica si una pieza puede moverse de su posición actual a otra casilla deseada
        movimientos_posibles = self.calcular_movimientos_posibles()
        return casilla_destino in movimientos_posibles 