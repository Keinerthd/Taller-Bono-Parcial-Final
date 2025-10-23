from DoubleLinkedList import DoubleLinkedList
from customer import Customer

list = DoubleLinkedList()

def add_customer(name, lastname, phone):
    """
    name = input("Digite el nombre del usuario ")
    lastname = input("Digite el apellido del usuario ")
    phone = input("Digite el telefono del usuario ")
    """
    id = input("Digite el id del usuario ")
    id = int (id)

    c1 = Customer(name, lastname, phone, id)
    id += 1

    list.append(c1)
   



# ---------------- CLIENTES ----------------
def registrar_cliente():
    
    name = input("Ingrese el nombre del cliente: ")
    lastname = input("Ingrese el apellido del cliente: ")
    phone = input("Ingrese el teléfono del cliente: ")
    add_customer(name, lastname, phone)
    print("Cliente registrado exitosamente.")
    

def listar_clientes():
    print("Lista de clientes registrados:")
    
    


def eliminar_cliente():   
    id = input("Ingrese el ID del cliente a eliminar: ")
    


    
# ---------------- MENÚ ----------------
def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1": registrar_cliente()
        elif opcion == "2": listar_clientes()
        elif opcion == "3": eliminar_cliente()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()