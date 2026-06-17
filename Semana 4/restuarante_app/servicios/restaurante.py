class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print(f"\n--- Menú de {self.nombre} ---")
        for p in self.productos:
            print(p)

    def mostrar_clientes(self):
        print(f"\n--- Clientes de {self.nombre} ---")
        for c in self.clientes:
            print(c)