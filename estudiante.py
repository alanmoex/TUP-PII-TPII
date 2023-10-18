from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, legajo: int, año_inscripcion_carrera: int) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self.__legajo = legajo
        self.__año_inscripcion_carrera = año_inscripcion_carrera
        self.__mis_cursos = [] #se podria colocar en usuario
    
    #getter y setter de legajo
    @property
    def legajo(self) -> int:
        return self.__legajo
    @legajo.setter
    def legajo(self, legajo:int):
        self.__legajo = legajo

    #getter y setter de año_inscripcion_carrera
    @property
    def año_inscripcion_carrera(self) -> int:
        return self.__año_inscripcion_carrera
    @año_inscripcion_carrera.setter
    def año_inscripcion_carrera(self, año_inscripcion_carrera:int):
        self.__año_inscripcion_carrera = año_inscripcion_carrera
    
    #-------------------------
    #falta getter de mis cursos
    #--------------------------

    def __str__(self) -> str:
        return super().__str__() + f" Legajo: {self.legajo}. Año de inscripción: {self.año_inscripcion_carrera}"
    
    def matricular_en_curso(self, curso:object) -> None:
        self.__mis_cursos.append(curso)

    