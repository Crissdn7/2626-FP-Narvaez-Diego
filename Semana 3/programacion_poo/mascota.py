class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):

        print("\n----------------------------------------")
        print(f"🐾 FICHA DE LA MASCOTA: {self.nombre.upper()}")
        print("----------------------------------------")
        print(f" -> Especie: {self.especie}")
        print(f" -> Edad:    {self.edad} años")
        print("----------------------------------------")

    def hacer_sonido(self):

        especie_limpia = self.especie.lower()

        if "perro" in especie_limpia:
            print(f"🔊 {self.nombre} dice: ¡Guau! ¡Guau!")
        elif "gato" in especie_limpia:
            print(f"🔊 {self.nombre} dice: ¡Miau! ¡Miau!")
        elif "loro" in especie_limpia or "ave" in especie_limpia or "pájaro" in especie_limpia:
            print(f"🔊 {self.nombre} dice: ¡Pío! ¡Pío! o ¡Quiiiq!")
        else:
            print(f"🔊 {self.nombre} hace un sonido nativo de su especie.")