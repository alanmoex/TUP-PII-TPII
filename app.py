from estudiante import Estudiante
from profesor import Profesor

lista_estudiantes= [Estudiante("alan", "moex", "alan@gmail.com", "alanmoex", "123", 2023)]
lista_profesores= [Profesor("Juan", "Perez", "juanperez@gmail.com", "juanperez", "licenciado", 2000)]

def menu_principal():
    print("1 - Ingresar cómo usuario")
    print("2 - Ingresar cómo profesor")
    print("3 - Ver cursos")
    print("4 - Salir")
def menu_estudiante():
    print("1 - Matricularse a un curso")
    print("2 - Ver curso")
    print("3 - Volver al menu principal")
def menu_profesor():
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3 - Volver al menu principal")

while True:
    menu_principal()
    op = int(input("Ingrese una opción\n"))
    if op == 1:
        encontrado = False
        email = str(input("Ingrese su email:\n"))
        contraseña = str(input("Ingrese su contraseña:\n"))
        for estudiante in lista_estudiantes:
            if estudiante.email == email:
                encontrado = True
                validado = estudiante.validar_credenciales(email, contraseña)
                if validado:
                    print("\nHa ingresado correctamente\n")
                    while True:
                        menu_estudiante()
                        opEst = int(input("Ingrese una opción\n"))
                        if opEst==1:
                            pass
                        elif opEst == 2:
                            pass
                        elif opEst == 3:
                            break

    elif  op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        print("\nEligio salir. chau")
        break
    else:
        print("Error, opcion ingresada incorrecta")