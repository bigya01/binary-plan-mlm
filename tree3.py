class Node:
    def __init__(self, val):
        """
        Initializes a node in the binary tree.

        Args:
            val: The value to be stored in the node.
        """
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self):
        """
        Inserts a new node into the binary tree.

        - If the tree is empty, prompts the user for the root value and creates the root node.
        - Otherwise, prompts the user for the parent key and the value to be inserted.
        - Searches for the parent node.
        - If the parent node is found, prompts the user for the side ('l' or 'r') to insert the new node and creates the new node as the left or right child of the parent.
        - If the parent node is not found, informs the user.
        """
        if self.root is None:
            val = int(input("Enter root value: "))
            self.root = Node(val)
        else:
            parent_key = int(input("Enter parent key: "))
            node = self.search(self.root, parent_key)
            if node is None:
                print("Parent key not found.")
            else:
                side = input("Insert in left or right (l/r)? ").lower()
                val = int(input("Enter value: "))
                if side == 'l':
                    if node.left is not None :
                        print ("items exist")
                    node.left = Node(val)
                elif side == 'r':
                    if node.right is not None :
                        node.right = Node(val)
                else:
                    print("Invalid side.")

    def search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
#     def display_helper(self,node, parent_val=None):
#         if node is None:
#             return
#         if parent_val is not None:
#             print(f"{parent_val} -> {node.val}")
#             print(f"{parent_val} -> {node.val}")  # Print connection to parent first
#   # Print connection to parent first
#         self.display_helper(node.left, node.val)  # Visit left child with current node as parent
#         self.display_helper(node.right, node.val)  # Visit right child with current node as parent
    
    def display_t(self, node):
        def display_h(node):
            if node is None:
                    return
            if node.left is not None:
                        print(f"{node.val} -> {node.left.val}")
            if node.right is not None:
                        print(f"{node.val} -> {node.right.val}")
            display_h(node.left)  
            display_h(node.right)  
        display_h(self.root)

tree = BinaryTree()

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tree.insert()
    elif choice == '2':
        key = int(input("Enter key to search: "))
        if tree.search(tree.root, key):
            print("Key found.")
        else:
            print("Key not found.")
    elif choice == '3':
        print("Tree structure: ")
        tree.display_t(tree.root)
        print()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")








#