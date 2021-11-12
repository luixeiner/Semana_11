empresas = {
    108212313: "Tecsup",
    424134134: "UdeA",
}

while True:
    # Creacion de menu
    print("\n"
          "Opcion 1) Registrar clientes \n"
          "Opcion 2) Mostrar clientes \n"
          "Opcion 3) Buscar clientes \n"
          "Opcion 4) Actualizar  clientes \n"
          "Opcion 5) Eliminar  clientes \n"
          "Opcion 6) Salir "
          )

    opcion = input("Escoja una opcion: ")

    if opcion == "1":
        ruc = int(input("Ingrese el RUC: "))
        nombre = input("Nombre de empresa: ")
        empresas[ruc] = nombre
    elif opcion == "2":
        print("Mostrar clientes", empresas)
    elif opcion == "3":
        nombre_cliente = str(input("Ingrese el ruc de la persona: "))
        print("resultado: ".empresas.get(nombre_cliente, "no se encontro" ))
    if opcion == "4":
        nuevo_cliente = input("Ingrese el ruc a modificar: ")
        nuevo_nombre = input ("Ingrese el nuevo numero del cliente")
        empresas[ruc] = nuevo_nombre
    elif opcion == "5":
        eliminar = str(input("Ingresa el numero ruc a eliminar"))
        del empresas[eliminar]
    elif opcion == "6":
        print("Adios")
        break
    