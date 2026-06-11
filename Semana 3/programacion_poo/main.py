from mascota import Mascota

if __name__ == "__main__":
    print("=== EJECUCIÓN DEL SISTEMA DE GESTIÓN DE MASCOTAS (POO) ===")

    mascota1 = Mascota("Luna", "Pato", 2)
    mascota2 = Mascota ("Leo", "Gato", 3)

    mascota1.mostrar_informacion()
    mascota1.hacer_sonido()

    mascota2.mostrar_informacion()
    mascota2.hacer_sonido()

    print("\n========================================================")