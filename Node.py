class Node:
    def __init__(self, data, next= None, prev= None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"Node({self.data!r})"