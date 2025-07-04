# models/persona.py

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, cedula: str, telefono: str):
        self._nombre = nombre
        self._apellido = apellido
        self._cedula = cedula
        self._telefono = telefono

    @abstractmethod
    def mostrar_info(self) -> str:
        """
        Método que debe ser implementado por todas las subclases para mostrar información.
        """
        pass
