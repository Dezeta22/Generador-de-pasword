import random
import numpy as np

def generar_password():
    letras_minusculas = [chr(i) for i in range(97, 123)]
    letras_mayusculas = [chr(i) for i in range(65, 91)]
    numeros = [str(i) for i in range(10)]
    caracteres = letras_minusculas + letras_mayusculas + numeros

    password = []
    
    # Primer carácter
    primer_caracter = random.choice(letras_mayusculas + letras_minusculas + numeros)
    password.append(primer_caracter)

    # Resto de caracteres
    length = random.randint(8, 15)
    for _ in range(length - 1):
        char = random.choice(caracteres)
        while char in password:
            char = random.choice(caracteres)
        password.append(char)

    # Números
    numeros_generados = 0
    while numeros_generados < 3:
        index = random.randint(0, len(password) - 1)
        if password[index].isdigit():
            continue
        password[index] = random.choice(numeros)
        numeros_generados += 1

    # Mayúsculas
    mayusculas_generadas = 0
    while mayusculas_generadas < 3:
        index = random.randint(0, len(password) - 1)
        if password[index].isupper():
            continue
        password[index] = random.choice(letras_mayusculas)
        mayusculas_generadas += 1

    # Mezclar los caracteres
    random.shuffle(password)

    return ''.join(password)


def main():
    password = generar_password()
    print("Contraseña generada:", password)


if __name__ == "__main__":
    main()

