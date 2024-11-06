from coordenada import Coordenada
from pieza import Pieza
from peon import Peon
from torre import Torre
from caballo import Caballo
from alfil import Alfil
from rey import Rey
from dama import Dama

def convertir_notacion(notacion):
    """
    Convierte notación algebraica de ajedrez (ej: 'b2') a coordenadas numéricas (fila, columna)
    """
    columnas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    columna = columnas[notacion[0].lower()]
    fila = int(notacion[1])
    return Coordenada(fila, columna)

def main():
    # Alfil
    un_alfil = Alfil("blanco", convertir_notacion("b2"))
    print(un_alfil.mover(convertir_notacion("d4")))
    print(un_alfil.mover(convertir_notacion("e4")))

    # Peón negro
    un_peon = Peon("negro", convertir_notacion("d2"))
    print(un_peon.mover(convertir_notacion("d1")))
    print(un_peon.mover(convertir_notacion("d4")))

    # Peón blanco
    un_peon = Peon("blanco", convertir_notacion("d4"))
    print(un_peon.mover(convertir_notacion("d5")))
    print(un_peon.mover(convertir_notacion("e6")))

    # Torre
    una_torre = Torre("blanco", convertir_notacion("d4"))
    print(una_torre.mover(convertir_notacion("d8")))
    print(una_torre.mover(convertir_notacion("e8")))

    # Dama
    una_dama = Dama("negro", convertir_notacion("b7"))
    print(una_dama.mover(convertir_notacion("h1")))
    print(una_dama.mover(convertir_notacion("e8")))

    # Caballo
    un_caballo = Caballo("negro", convertir_notacion("a1"))
    print(un_caballo.mover(convertir_notacion("b3")))
    print(un_caballo.mover(convertir_notacion("b2")))

    # Rey
    mi_rey = Rey("negro", convertir_notacion("e3"))
    print(mi_rey.mover(convertir_notacion("f3")))
    print(mi_rey.mover(convertir_notacion("b2")))

if __name__ == "__main__":
    main()