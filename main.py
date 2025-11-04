import os
from datetime import datetime

def menu():
    print("\n              MENÚ PRINCIPAL")
    print("-"*45)
    print("0. Salir")
    print("1. Listar el contenido del directorio actual.")
    print("2. Crear una nueva carpeta.")
    print("3. Crear un archivo de texto.")
    print("4. Escribir un texto en un archivo existente.")
    print("5. Eliminar el archivo o carpeta.")
    print("6. Mostrar la información del archivo.")
    print("7. Navegar al directorio anterior.")

def listar_contenido():
    pass
def crear_directorio():
    pass
def crear_archivo():
    pass
def escribir_texto():
    pass
def eliminar():
    pass
def mostrar_info():
    pass
def main():
    while True:
        print(f"\n Ruta actual: {os.getcwd()}")
        menu()
        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        elif opcion == "1":
            listar_contenido()

        elif opcion == "2":
            crear_directorio()

        elif opcion == "3":
            crear_archivo()

        elif opcion == "4":
            escribir_texto()

        elif opcion == "5":
            eliminar()

        elif opcion == "6":
            mostrar_info()

        elif opcion == "7":
            try:
                os.chdir('..')
                print("Navegando al director anterior.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()