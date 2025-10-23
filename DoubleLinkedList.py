from Node import Node
from customer import Customer

class DoubleLinkedList:

    def __init__(self):
        self.tail = None
        self._size = 0

    def preprend(Self, new_node):
        
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            new_node.prev = self.tail
            self.head.prev = self.tail

        self.head = new_node
        self._size += 1


    def append_tail(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            new_node.prev = None
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

id = input ("digite el id del usuario")
name = input("Digite el nombre del usuario")
lastname = input("Digite el apellido del usuario")
phone = input("Digite el telefono del usuario")

c1 = Customer(id, name, lastname, phone)
c2 = Customer(id, name, lastname, phone)
c3 = Customer(id, name, lastname, phone)


sll = DoubleLinkedList()
sll.prepend(5)
sll.prepend(3)
sll.prepend(2)
sll.prepend(1)
sll.prepend(0)

