from usuario import Usuario

lista_estudiantes= []
lista_profesores= []

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
        email = str(input("Ingrese su email:\n"))
        contraseña = str(input("Ingrese su contraseña:\n"))
        for estudiante in lista_estudiantes:
            if estudiante.email == email:
                pass
    elif  op == 2:
        pass
    elif op == 3:
        pass
    elif op == 4:
        print("\nEligio salir. chau")
        break
    else:
        print("Error, opcion ingresada incorrecta")