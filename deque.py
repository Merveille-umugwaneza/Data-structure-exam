from collections import deque

class ApplianceCatalog:
    def __init__(self, max_capacity=None):
        """
        Initializes the catalog.
        :param max_capacity: Optional maximum capacity of the catalog (None for unlimited).
        """
        self.catalog = deque(maxlen=max_capacity)

    def add_appliance(self, appliance_name, appliance_type, brand, price):
        """
        Adds a new appliance to the catalog.
        :param appliance_name: Name of the appliance.
        :param appliance_type: Type of the appliance (e.g., Refrigerator, Oven).
        :param brand: Brand of the appliance.
        :param price: Price of the appliance.
        """
        appliance = {
            "name": appliance_name,
            "type": appliance_type,
            "brand": brand,
            "price": price,
        }
        self.catalog.append(appliance)
        print(f"Added: {appliance}")

    def remove_oldest(self):
        """
        Removes the oldest appliance from the catalog.
        """
        if self.catalog:
            removed = self.catalog.popleft()
            print(f"Removed oldest appliance: {removed}")
        else:
            print("Catalog is empty. Nothing to remove.")

    def remove_newest(self):
        """
        Removes the most recently added appliance from the catalog.
        """
        if self.catalog:
            removed = self.catalog.pop()
            print(f"Removed newest appliance: {removed}")
        else:
            print("Catalog is empty. Nothing to remove.")

    def view_catalog(self):
        """
        Displays the current catalog.
        """
        if self.catalog:
            print("\nCurrent Catalog:")
            for index, appliance in enumerate(self.catalog, start=1):
                print(f"{index}. {appliance}")
        else:
            print("Catalog is empty.")

if __name__ == "__main__":
    catalog = ApplianceCatalog(max_capacity=5)  

    catalog.add_appliance("Refrigerator", "Cooling", "Samsung", 1200)
    catalog.add_appliance("Microwave", "Cooking", "Panasonic", 300)
    catalog.add_appliance("Dishwasher", "Cleaning", "Bosch", 800)
    catalog.add_appliance("Washing Machine", "Laundry", "LG", 700)
    catalog.add_appliance("Air Conditioner", "Cooling", "Daikin", 1000)

    catalog.view_catalog()

    catalog.add_appliance("Blender", "Cooking", "Philips", 150)
    catalog.view_catalog()

    catalog.remove_oldest()
    catalog.remove_newest()
    catalog.view_catalog()
