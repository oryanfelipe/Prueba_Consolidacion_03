nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

cientificos = []
magos = []
otros = []

for nombre in nombres:
    if nombre in ["Newton", "Einstein", "Hawking"]:
        cientificos.append(nombre)
    elif nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    else:
        otros.append(nombre)
print("Cientificos:", cientificos)
print("Magos:", magos)
print("Otros:", otros)

#Funcion1
def hacer_grandioso(magos):
    for i in range(len(magos)):
        if not magos[i].startswith("El gran"):
            magos[i] = "El gran " + magos[i]
        

magos = ["Harry Houdini", "David Blaine", "Teller"]
hacer_grandioso(magos)
print(magos)


#Funcion2
def imprimir_nombres(nombres):
    for i in range(len(nombres)):
        print(nombres[i])

#Funcion3
def imprime_todos():
    print("Lista completa de nombres:")
    imprimir_nombres(nombres)
    print()

    print("Magos grandiosos:")
    hacer_grandioso(magos)
    imprimir_nombres(magos)
    print()

    print("Cientificos:")
    imprimir_nombres(cientificos)
    print()

    print("Otros:")
    imprimir_nombres(otros)
    
imprime_todos()
print()