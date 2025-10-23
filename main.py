
from Customer import Customer

def add_customer(name, lastname, phone):
    id = input ("digite el id del usuario ")
    name = input("Digite el nombre del usuario ")
    lastname = input("Digite el apellido del usuario ")
    phone = input("Digite el telefono del usuario ")

    c1 = Customer(id, name, lastname, phone)
    c2 = Customer(id, name, lastname, phone)
    c3 = Customer(id, name, lastname, phone)


    sll = DoubleLinkedList()
    sll.preprend(c1)
    sll.preprend(c2)
    sll.preprend(c3)

    print(sll)



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