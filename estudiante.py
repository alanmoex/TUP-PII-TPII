from usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contraseña: str, legajo: int, año_inscripcion_carrera: int, carrera: object) -> None:
        super().__init__(nombre, apellido, email, contraseña)
        self.__legajo = legajo
        self.__año_inscripcion_carrera = año_inscripcion_carrera
        self.__mis_cursos = []
        self.__carrera = carrera

    @property
    def legajo(self) -> int:
        return self.__legajo
    
    @legajo.setter
    def legajo(self, legajo: int):
        self.__legajo = legajo

    @property
    def año_inscripcion_carrera(self) -> int:
        return self.__año_inscripcion_carrera
    
    @año_inscripcion_carrera.setter
    def año_inscripcion_carrera(self, año_inscripcion_carrera: int):
        self.__año_inscripcion_carrera = año_inscripcion_carrera

    @property
        return self.__mis_cursos

    @mis_cursos.setter
    def mis_cursos(self, mis_cursos: object):
        self.__carrera = mis_cursos

    @property
    def carrera(self) -> object:
        return self.__carrera
    
    @carrera.setter
    def carrera(self, carrera: object):
        self.__carrera = carrera


    def __str__(self) -> str:
        return super().__str__() + f" Legajo: {self.legajo}. Año de inscripción: {self.año_inscripcion_carrera}"

    def matricularse_en_curso(self, curso: object, contra: str) -> str:
        if curso in self.mis_cursos:
            return "\nYa estás matriculado en este curso.\n"        
        if contra == curso.contraseña_matriculacion:
            self.mis_cursos.append(curso)
            return f"\nTe has matriculado en el curso: {curso.nombre}.\n"
        else:
            return "La contraseña de matriculación es incorrecta."
