class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None

    def add(self, data):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, key):

        current = self.head
        
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            print("Key not found in the list.")
            return
        
        prev.next = current.next
        current = None

    def display(self):
        
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(nodes))


if __name__ == "__main__":
    catalog = SinglyLinkedList()
    
    catalog.add("Refrigerator")
    catalog.add("Washing Machine")
    catalog.add("Microwave Oven")
    catalog.add("Air Conditioner")
    
    print("Catalog:")
    catalog.display()

    catalog.remove("Microwave Oven")
    print("\nCatalog after removing 'Microwave Oven':")
    catalog.display()