from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from archivo import Archivo
from data import *

tup = Carrera("Tecnicatura Universitaria en Programación", 2)
tup.agregar_curso(Curso(tup, "programacion 1"))

lista_carreras = [tup]

lista_estudiantes = [Estudiante("alan", "moex", "alan@gmail.com", "alanmoex", 123, 2023, tup)]
lista_profesores = [Profesor("Juan", "Perez", "juanperez@gmail.com", "juanperez", "licenciado", 2000)]