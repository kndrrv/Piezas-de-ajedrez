# Kendra Gutiérrez Vega, 2024

class Coordenada: # se crea la clase coordenada
    def __init__(self, fila, columna): # se utiliza el constructor y se le añaden los parámetros
        self.__fila = fila # se agregan los atributos utilizando self para acceder a ellos y __ para hacerlos privados
        self.__columna = columna

    def __eq__(self, otra): # se utiliza el método __eq__ para comparar si son iguales
        if not isinstance(otra, Coordenada): # verifica que el objeto esté en la misma instancia de la clase
            return False
        return self.__fila == otra.__fila and self.__columna == otra.__columna # compara la fila y la columna
    
    # getter y setter de fila
    def get_fila(self): # se utiliza el método getter para poder acceder al atributo __fila
        return self.__fila 
    
    def set_fila(self, new_fila): # se utiliza el método setter para modificar el atributo __fila
        self.__fila = new_fila

    # getter y setter de columna
    def get_columna(self): # se utiliza el método getter para poder acceder al atributo __columna
        return self.__columna
    
    def set_columna(self, new_columna): # se utiliza el método setter para acceder al atributo __columna
        self.__columna = new_columna

    def __str__(self):
        return f"Fila: {self.__fila} Columna: {self.__columna}"
    