def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = input("Ingrese la edad: ")

    return {"nombre": nombre, "especie": especie, "edad": edad}


def mostrar_mascota(mascota):
    print("\n--------------------------")
    print(" INFORMACIÓN DE LA MASCOTA ")
    print("--------------------------")
    print(f"Nombre : {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad   : {mascota['edad']} años")


if __name__ == "__main__":
    datos_mascota = registrar_mascota()
    mostrar_mascota(datos_mascota)