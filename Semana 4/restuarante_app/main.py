from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def run():
    mi_restaurante = Restaurante("Restaurante Raices")

    p1 = Producto("Encebollado", 5.00)
    p2 = Producto("Bolon", 2.50)
    c1 = Cliente("Diego Narváez", "diego123@gmail.com")

    mi_restaurante.agregar_producto(p1)
    mi_restaurante.agregar_producto(p2)
    mi_restaurante.registrar_cliente(c1)

    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    run()