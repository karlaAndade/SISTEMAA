# models/resultado.py

from models.examen import Examen

class Resultado:
    def __init__(self, examen: Examen, valor_obtenido: float):
        self.__examen = examen
        self.__valor_obtenido = valor_obtenido

    def es_normal(self) -> bool:
        """
        Verifica si el valor está dentro del rango normal del examen asociado.
        """
        return self.__examen.es_valor_normal(self.__valor_obtenido)

    def mostrar_detalle(self) -> str:
        estado = "Normal" if self.es_normal() else "Fuera de rango"
        return f"{self.__examen.obtener_nombre()}: {self.__valor_obtenido} {estado}"
