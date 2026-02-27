import os

def limpiar():
    os.system("cls")

def menu():
    while True:
        print("1. saludar")
        print("2. despedir")
        print("3. Salir\n")

        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                limpiar()
                print("Hola, bienvenid@ a la mejor clase de git")
                input("Presione Enter para continuar...")
            case 2:
                limpiar()
                print("Adiós, gracias por participar en la mejor clase de git")
                input("Presione Enter para continuar...")
            case 3:
                limpiar()
                input("Saliendo del programa...")
                break
            case _:
                limpiar()
                print("Opción no válida, por favor intente de nuevo")
                input("Presione Enter para continuar...")

if __name__ == "__main__":
    limpiar()
    menu()