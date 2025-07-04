# models/usuario_sistema.py

from models.persona import Persona  # Asegúrate de que esta ruta sea válida

class UsuarioSistema:
    def __init__(self, nombre_usuario: str, contrasena: str, persona: Persona):
        self.__nombre_usuario = nombre_usuario
        self.__contrasena = contrasena
        self.__persona = persona

    def verificar_credenciales(self, usuario: str, contrasena: str) -> bool:
        return self.__nombre_usuario == usuario and self.__contrasena == contrasena

    def mostrar_rol(self) -> str:
        return self.__persona.__class__.__name__.lower()  # ejemplo: 'paciente', 'medico'

    def get_persona(self) -> Persona:
        return self.__persona
