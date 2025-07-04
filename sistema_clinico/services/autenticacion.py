# services/autenticacion.py

from models.usuario_sistema import UsuarioSistema

class ServicioAutenticacion:
    def __init__(self):
        self.__usuarios = []

    def registrar_usuario(self, usuario: UsuarioSistema):
        self.__usuarios.append(usuario)

    def autenticar(self, nombre_usuario: str, contrasena: str) -> UsuarioSistema | None:
        for usuario in self.__usuarios:
            if usuario.verificar_credenciales(nombre_usuario, contrasena):
                return usuario
        return None
