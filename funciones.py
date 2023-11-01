from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from archivo import Archivo
from data import *

def menu_principal():
    print("\n1 - Ingresar como estudiante")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_estudiante():
    print("\n1 - Matricularse en un curso")
    print("2 - Desmatricularse en un curso")
    print("3 - Ver cursos matriculados")
    print("4 - Volver al menú principal")

def menu_profesor():
    print("\n1 - Dictar curso")
    print("2 - Ver cursos")
    print("3 - Volver al menú principal")

def validar_rango_enteros(menor, mayor):
    while True:
        opcion = input("\nIngrese una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if menor <= opcion <= mayor:
                return opcion
            else:
                print("\nError: Ingrese una opción válida.")
        else:
            print("\nError: Ingrese un número.")

def login(lista_usuarios:list) -> object:
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    encontrado = False

    for usuario in lista_usuarios:
        if usuario.email == email:
            encontrado = True
            if usuario.validar_credenciales(email, contraseña):
                print("\nHa ingresado correctamente.\n")
                return usuario
            else:
                print("\nError: Contraseña incorrecta.\n")
                return None

    if not encontrado and lista_usuarios == lista_profesores:
        print("\nUsuario no encontrado")
        codigo = input("\nIngrese el codigo para darse de alta como profesor:\n")
        if codigo == "admin":
            nombre = input("Ingrese su nombre:")
            apellido = input("Ingrese su apellido:")
            email = input("Ingrese su email:")
            contraseña = input("Ingrese su contraseña:")
            titulo = input("Ingrese su titulo:")
            año_egreso = int(input("Ingrese su año de egreso:"))
            nuevo_profesor = Profesor(nombre,apellido,email,contraseña,titulo,año_egreso)
            lista_usuarios.append(nuevo_profesor)
            return None
        else:
            print("\nCodigo incorrecto\n")
            return None
    if not encontrado:
        print("\nUsuario no encontrado. Debe darse de alta en alumnado.\n")
        return None
    
def imprimir_cursos(lista_cursos):
    for n, curso in enumerate(lista_cursos, 1):
        print(f"{n} {curso.nombre}")

def matricularse(estudiante:object): 
    if not estudiante.carrera.cursos:
        print("\nAdvertencia: No hay cursos creados en la carrera.\n")
    else:
        print("\nCursos disponibles:")
        imprimir_cursos(estudiante.carrera.cursos)
        opcion = validar_rango_enteros(1,len(estudiante.carrera.cursos))
        curso = estudiante.carrera.cursos[opcion-1]
        print(str(curso)) #debugginh
        contra = input("Ingrese la contraseña de matriculación del curso: ")
        mensaje = estudiante.matricularse_en_curso(curso, contra)
        print(mensaje)


def desmatricularse(estudiante:object): 
    if not estudiante.mis_cursos:
        print("\nNo estás matriculado en ningún curso.\n")
    else:
        print("Cursos matriculados:")
        imprimir_cursos(estudiante.mis_cursos)
        opcion = validar_rango_enteros(1,len(estudiante.mis_cursos))
        curso = estudiante.mis_cursos[opcion-1]
        estudiante.desmatricularse_en_curso(curso)
        print("Te has desmatriculado correctamente")

def ver_cursos(usuario:object):
    if not usuario.mis_cursos:
        print("\nNo estás matriculado en ningún curso.\n")
    else:
        print("Tus cursos:")
        imprimir_cursos(usuario.mis_cursos)
        opcion = validar_rango_enteros(1, len(usuario.mis_cursos))
        curso = usuario.mis_cursos[opcion - 1]
        if isinstance(usuario, Estudiante):
            if not curso.archivos:
                print("\nNo hay archivos subidos en este curso\n")
            else:
                archivos_ordenados = sorted(curso.archivos, key=lambda archivo: archivo.fecha)
                print(curso.nombre)
                for archivo in archivos_ordenados:
                    print(archivo)
        if isinstance(usuario, Profesor):
            print(f"{curso}\nCantidad de archivos: {len(curso.archivos)}")
            print("\nDesea agregar un archivo?\n1-si\n2-no")
            opcion = validar_rango_enteros(1,2)
            if opcion == 1:
                nombre = input("Ingrese el nombre del archivo:")
                formato = input("ingrese el formato del archivo:")
                archivo = Archivo(nombre,formato)
                curso.nuevo_archivo(archivo)
    
def dictar_curso(profesor:object):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    encontrado = False
    for carrera in lista_carreras:
        if nombre_carrera == carrera.nombre:
            encontrado = True
            nombre_curso = input("Ingrese el nombre del nuevo curso: ")
            nuevo_curso = Curso(carrera, nombre_curso)
            profesor.dictar_curso(nuevo_curso)
            carrera.agregar_curso(nuevo_curso)
            print(nuevo_curso)
            break
    if not encontrado:
        print("\nLa carerra ingresada no existe\n")