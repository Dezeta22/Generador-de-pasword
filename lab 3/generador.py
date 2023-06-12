#generador.py llamamos la funcion "generar password" de el archvo "generadir_password.py" 
from generador_password import generar_password

def main():
    password = generar_password()
    print("Contraseña generada:", password)

if __name__ == "__main__":
    main()
