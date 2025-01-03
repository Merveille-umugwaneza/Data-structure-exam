class TreeNode:
    def __init__(self, name, details=None):
        """
        Initialize a node in the tree.

        :param name: Name of the category, subcategory, or product
        :param details: Additional information about the node (optional, for products)
        """
        self.name = name
        self.details = details  
        self.children = []  

    def add_child(self, child_node):
        """
        Add a child node to the current node.

        :param child_node: A TreeNode instance
        """
        self.children.append(child_node)

    def display_tree(self, level=0):
        """
        Recursively display the tree structure.

        :param level: The current depth in the tree
        """
        prefix = " " * (level * 4)  
        print(f"{prefix}- {self.name}")
        if self.details:
            print(f"{prefix}  Details: {self.details}")
        for child in self.children:
            child.display_tree(level + 1)

if __name__ == "__main__":

    catalog = TreeNode("Home Appliances Catalog")

    kitchen_appliances = TreeNode("Kitchen Appliances")
    living_room_appliances = TreeNode("Living Room Appliances")
    catalog.add_child(kitchen_appliances)
    catalog.add_child(living_room_appliances)

    refrigerators = TreeNode("Refrigerators")
    ovens = TreeNode("Ovens")
    fans = TreeNode("Fans")
    air_conditioners = TreeNode("Air Conditioners")
    kitchen_appliances.add_child(refrigerators)
    kitchen_appliances.add_child(ovens)
    living_room_appliances.add_child(fans)
    living_room_appliances.add_child(air_conditioners)

    refrigerators.add_child(TreeNode("Samsung Fridge", {"Price": "$1200", "Capacity": "400L"}))
    refrigerators.add_child(TreeNode("LG Fridge", {"Price": "$1000", "Capacity": "350L"}))
    ovens.add_child(TreeNode("Panasonic Microwave", {"Price": "$200", "Power": "800W"}))
    fans.add_child(TreeNode("Dyson Fan", {"Price": "$300", "Features": "Bladeless"}))
    air_conditioners.add_child(TreeNode("Daikin AC", {"Price": "$600", "Capacity": "1.5 Ton"}))


    catalog.display_tree()
