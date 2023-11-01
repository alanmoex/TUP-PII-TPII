from estudiante import Estudiante
from profesor import Profesor
from curso import Curso
from carrera import Carrera
from archivo import Archivo
from funciones import *

while True:
    menu_principal()
    op = validar_rango_enteros(1,4)

    if op == 1:
        estudiante = login(lista_estudiantes)
        if estudiante:
            while True:
                menu_estudiante()
                opEst = validar_rango_enteros(1,4)
                
                if opEst == 1:
                    matricularse(estudiante)     
                elif opEst == 2:
                    desmatricularse(estudiante)             
                elif opEst == 3:
                    ver_cursos(estudiante)
                elif opEst == 4:
                    break
               
    elif op == 2:
        profesor = login(lista_profesores)
        if profesor:
            while True:
                menu_profesor()
                opProf = validar_rango_enteros(1,4)

                if opProf == 1:
                    dictar_curso(profesor)
                elif opProf == 2:
                    ver_cursos(profesor)
                elif opProf == 3:
                    break        
    
    elif op == 3:
        lista_cursos = [curso for carrera in lista_carreras for curso in carrera.cursos]
        if not lista_cursos:
            print("Advertencia: No hay cursos creados en el sistema.")
        else:
            cursos_ordenados = sorted(lista_cursos, key=lambda curso: curso.nombre)
            for curso in cursos_ordenados:
                print(f"Materia: {curso.nombre.ljust(30)} Carrera: {curso.carrera.nombre}") #el metodo ljust(n) da un ancho de caracteres (n) fijos para la cadena
    
    elif op == 4:
        print("Ha elegido salir. Chau")
        break

    else:
        print("Error: opción ingresada incorrecta.")
