class Libro:
    """
    Clase que representa un objeto del mundo real: un Libro.
    """
    # Constructor de la clase (Definición de atributos)
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True

    # Método 1: Prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"Éxito: El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"Error: El libro '{self.titulo}' ya se encuentra prestado actualmente.")

    # Método 2: Devolver el libro
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f"Éxito: El libro '{self.titulo}' ha sido devuelto y ahora está disponible.")
        else:
            print(f"Información: El libro '{self.titulo}' ya estaba en la biblioteca.")

    # Método extra para mostrar la información formateada del libro
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Libro: '{self.titulo}' | Autor: {self.autor} | Páginas: {self.paginas} | Estado: {estado}")


# --- EJECUCIÓN PRINCIPAL DEL PROGRAMA ---
if __name__ == "__main__":
    print("--- REGISTRO Y GESTIÓN DE LIBROS --- \n")

    # Requerimiento: Creación de al menos dos objetos diferentes
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 496)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 864)

    # Mostrando información inicial de los objetos creados
    print("Estado inicial de los libros:")
    libro1.mostrar_informacion()
    libro2.mostrar_informacion()
    print("-" * 50)

    # Demostración del funcionamiento de los métodos
    print("Acciones sobre el Libro 1:")
    libro1.prestar()
    libro1.mostrar_informacion()
    libro1.prestar()
    print("-" * 50)

    print("Acciones sobre el Libro 2:")
    libro2.devolver()
    libro2.prestar()
    libro2.mostrar_informacion()
    libro2.devolver()
    libro2.mostrar_informacion()
    print("-" * 50)