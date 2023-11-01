from usuario import Usuario
from curso import Curso

class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, titulo: str, año_egreso: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self.__titulo = titulo
        self.__año_egreso = año_egreso
        self.__mis_cursos = []

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def año_egreso(self) -> int:
        return self.__año_egreso

    @año_egreso.setter
    def año_egreso(self, año_egreso: int):
        self.__año_egreso = año_egreso

    @property
    def mis_cursos(self):
        return self.__mis_cursos

    def __str__(self) -> str:
        return super().__str__() + f" Título: {self.titulo}. Año de egreso: {self.año_egreso}"

    def dictar_curso(self, curso:object):
        self.__mis_cursos.append(curso)
        print(f"Curso {curso.nombre} dado de alta con éxito.")

