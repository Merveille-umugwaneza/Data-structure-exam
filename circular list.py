class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def add_item(self, data):
        new_node = Node(data)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def display_catalog(self):
        if not self.last:
            print("Catalog is empty.")
            return

        current = self.last.next
        print("Home Appliances Catalog:")
        while True:
            print(f"- {current.data}")
            current = current.next
            if current == self.last.next:
                break

    def delete_item(self, key):
        if not self.last:
            print("Catalog is empty.")
            return

        current = self.last.next
        prev = self.last

        while True:
            if current.data == key:
                if current == self.last and current.next == self.last:
                    self.last = None
                else:
                    prev.next = current.next
                    if current == self.last:
                        self.last = prev
                print(f"Item '{key}' deleted.")
                return
            elif current == self.last:
                break
            prev = current
            current = current.next

        print(f"Item '{key}' not found.")


catalog = CircularLinkedList()
catalog.add_item("Refrigerator")
catalog.add_item("Washing Machine")
catalog.add_item("Microwave")
catalog.add_item("Air Conditioner")

catalog.display_catalog()

catalog.delete_item("Microwave")
catalog.display_catalog()
