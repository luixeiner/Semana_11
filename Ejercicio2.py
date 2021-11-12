usuarios = {}

while True:
    email = input("Ingrese un email: ")
    password = input("Contraseña: ")
    # verificar si el email existe
    if usuarios.get(email) is None:
        usuarios[email] = password
    else:
        print("El email ya existe")

    opcion = input("Desea ingresar otro email? (si/no) ")
    if opcion == "no":
        print("Usuarios registrados: ", usuarios)
        break
