import os
import time
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
    try:
        contenido = os.listdir(os.getcwd())
        if not contenido:
            print("El directorio está vacío")
        else:
            print("Contenido del directorio:")
            for elemento in contenido:
                if os.path.isdir(elemento):
                    print(f"CARPETA] -> {elemento}")
                else:
                    print(f"[ARCHIVO] -> {elemento}")

    except Exception as e:
        print(f"Error. {e}")


def crear_directorio():
    nombre = input("Introduce el nombre de la carpeta que quieres crear: ")
    try:
        if os.path.exists(nombre):
            print("Ya existe una carpeta con ese nombre. Prueba otro.")
        else:
            os.mkdir(nombre)
            print(f"Carpeta {nombre} creada corrrectamente.")
    except Exception as e:
        print(f"Error. {e}")


def crear_archivo():
    nombre = input("Intrdoduce un nombre para el archivo a crear con su extensión (.txt)")
    try:
        if os.path.exists(nombre):
            print("Ya existe una archivo con ese nombre. Prueba otro.")
            return
        contenido = input("Introduce el contenido del archivo: ")
        with open(nombre, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)
        print(f"Archivo {nombre} creado correctamente.")
    except Exception as e:
        print(f"Error. {e}")


def escribir_texto():
    nombre = input("Introduce el nombre del archivo en el que deseas escribir: ")
    try:
        if os.path.exists(nombre):
            print("Ya existe una archivo con ese nombre. Prueba otro.")
            return
        texto_a_escribir = input("Introduce el texto que deseas añadir: ")
        with open(nombre, "a", encoding="utf-8") as archivo:
            archivo.write(f"\n{texto_a_escribir}")
        print(f"Texto añadido al archivo {nombre} correctamente.")
    except Exception as e:
        print(f"Error. {e}")


def eliminar():
    nombre = input("Introduce el nombre de la carpeta a eliminar: ")
    try:
        if not os.path.exists(nombre):
            print("El archivo o carpeta no existe.")
            return
        if os.path.isdir(nombre):
            os.rmdir(nombre)
            print(f"Carpeta {nombre} eliminada correctamente.")
        else:
            os.remove(nombre)
            print(f"Archivo {nombre} eliminado correctamente.")
    except OSError as e:
        print(f"No se puede eliminar {nombre}. Asegúrate de que esté vacío si es una carpeta.")
    except Exception as e:
        print(f"Error. {e}")


def mostrar_info():
    nombre = input("Introduce el nombre del archivo o carpeta que quieres analizar: ")
    try:
        if not os.path.exists(nombre):
            print("El archivo o carpeta no existe.")
            return
        tamano = os.path.getsize(nombre)
        fecha_mod = time.ctime(os.path.getmtime(nombre))
        tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"

        print(f"Información de {nombre}")
        print(f"Tipo: {tipo}")
        print(f"Tamaño: {tamano} bytes")
        print(f"Ultima modificación: {fecha_mod}")

    except Exception as e:
        print(f"Error. {e}")


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