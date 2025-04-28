import string
import random

def generar_contrasena(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("--- Generador de Contraseñas Seguras ---")
    try:
        longitud = int(input("¿De cuántos caracteres quieres la contraseña? (8-64): "))
        if 8 <= longitud <= 64:
            contrasena = generar_contrasena(longitud)
            print(f"\nTu nueva contraseña segura es:\n{contrasena}")
        else:
            print("Error: Elige un número entre 8 y 64.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
