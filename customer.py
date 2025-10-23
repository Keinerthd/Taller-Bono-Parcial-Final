from Node import Node
class Customer(Node):
    
    def __init__(self, name, lastname, phone, isActive, id=0):
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.isActive = isActive 
        self.id = id
    

    def __repr__(self):
        return f"Customer(id={self.id!r}, name={self.name!r}, lastname={self.lastname!r}, phone={self.phone!r}, isActive={self.isActive!r})"



