from Node import Node
from customer import Customer

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(repr(current))
            current = current.next
        return " <-> ".join(nodes)

    def preprend(self, new_node):
        
        node = Node(new_node)
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

"""
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
"""
