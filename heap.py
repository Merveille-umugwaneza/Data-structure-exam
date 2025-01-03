import heapq

class FixedSizeOrderHeap:
    def __init__(self, capacity):
        """
        Initializes the heap with a fixed capacity.
        :param capacity: The maximum number of orders the heap can hold.
        """
        self.capacity = capacity
        self.heap = []  
    
    def add_order(self, priority, order_details):
        """
        Adds an order to the heap.
        :param priority: The priority value of the order (e.g., order amount).
        :param order_details: A description or details of the order.
        """
        
        heapq.heappush(self.heap, (priority, order_details))
        
        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)
    
    def get_orders(self):
        """
        Retrieves all orders from the heap, sorted by priority.
        :return: A list of orders sorted by priority in ascending order.
        """
        return sorted(self.heap)

    def __str__(self):
        """
        Returns a string representation of the heap.
        """
        return f"FixedSizeOrderHeap(capacity={self.capacity}, orders={self.get_orders()})"

if __name__ == "__main__":
    order_heap = FixedSizeOrderHeap(3)  
    

    order_heap.add_order(100, "Order 1: Washing Machine")
    order_heap.add_order(200, "Order 2: Refrigerator")
    order_heap.add_order(50, "Order 3: Microwave Oven")
    order_heap.add_order(300, "Order 4: Air Conditioner")
    order_heap.add_order(150, "Order 5: Dishwasher")
    
    print("Current orders in the heap:")
    for priority, details in order_heap.get_orders():
        print(f"Priority: {priority}, Details: {details}")
