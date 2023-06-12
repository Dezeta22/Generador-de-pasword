from validador_password import validar_password 

# Colocamos aquí el código que deseamos que se ejecute al iniciar el programa
def main():
    password = input("Ingresa la password a validar: ")
    es_valido, mensaje = validar_password(password)
    print(mensaje)

# Verificamos si el archivo se ejecuta directamente o se importa como módulo
if __name__ == "__main__":
    main()
