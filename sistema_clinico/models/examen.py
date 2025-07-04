# models/examen.py

class Examen:
    def __init__(self, nombre: str, unidad: str, valor_minimo: float, valor_maximo: float, precio: float):
        self.__nombre = nombre
        self.__unidad = unidad
        self.__valor_minimo = valor_minimo
        self.__valor_maximo = valor_maximo
        self.__precio = precio

    def es_valor_normal(self, valor: float) -> bool:
        """
        Determina si el valor está dentro del rango normal del examen.
        """
        return self.__valor_minimo <= valor <= self.__valor_maximo

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_precio(self) -> float:
        return self.__precio
