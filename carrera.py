class Carrera:
    def __init__(self, nombre:str, cant_anios:int) -> None:
        self.__nombre = nombre
        self.__cant_anios = cant_anios
        self.__cursos = []
        self.__inscriptos = []
    
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre
    
    @property
    def cant_anios(self) -> int:
        return self.__cant_anios

    @cant_anios.setter
    def cant_anios(self, cant_anios: int):
        self.__cant_anios = cant_anios
    
    @property
    def cursos(self) -> list:
        return self.__cursos

    def __str__(self) -> str:
        return f"Carrera: {self.nombre}. Cantidad de años: {self.cant_anios}"

    def get_cantidad_materias(self) -> int:
        return len(self.cursos)
    
    def agregar_curso(self, curso) -> None:
        self.cursos.append(curso)