
alumnos = {
    'alumno1': 'fernando sanches',
    'alumno2': 'vannesa chque',
    'alumno3': 'yerly moreno',
    'alumno4': 'ana salas',
    'alumno5': 'luis corrales',
}
print(alumnos)
# len() es la funcion que se encarga de contar
# cuantos elementos tiene un diccionario
print(len(alumnos))
# Imprimir solo claves
print(alumnos.keys())
# Imprimir los valores
print(alumnos.values())

# version 1
print(alumnos['alumno1'])

print("*"*30)
for key in alumnos.keys():
    print(alumnos[key])

print("*"*30)

alumnos['alumno6'] = 'Lucas Solano'


alumnos_nuevos = {
    'alumno7': 'Carla Ferndez'
}

alumnos.update(alumnos_nuevos)

print("*"*30)
print(alumnos)

del alumnos['alumno6']

# En esta fase alumnos si tiene valores
alumnos_copy = alumnos.copy()

# Luego de asignar los valores a copy recien se esta eliminando
# alumnos
alumnos.clear()

print("*"*30)
print(alumnos)
print("alumnos_copy")
print("* "*30)
print(alumnos_copy)


# Convertir un diccionario a u tuplas
print(alumnos_copy.items())
print("* "*30)
print(alumnos_nuevos)