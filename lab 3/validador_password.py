def validar_password(password):
    if len(password) < 8 or len(password) > 15:
        return False, "La longitud debe estar entre 8 y 15 caracteres."

    if not any(c.isupper() for c in password):
        return False, "Debe haber al menos  1 letra mayúscula."

    if sum(c.isdigit() for c in password) != 3:
        return False, "Debe haber exactamente 3 números."

    if len(set(password)) != len(password):
        return False, "No se permiten caracteres repetidos."

    return True, "El password cumple con todas las validaciones."


def main():
    password = input("Ingresa la password a validar: ")
    es_valido, mensaje = validar_password(password)
    print(mensaje)


if __name__ == "__main__":
    main()
