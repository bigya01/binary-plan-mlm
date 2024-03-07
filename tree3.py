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
                    node.left = Node(val)
                elif side == 'r':
                    node.right = Node(val)
                else:
                    print("Invalid side.")

    def search(self, node, key):
        """
        Searches for a node with the given key in the binary tree.

        Args:
            node: The current node to search.
            key: The key value to search for.

        Returns:
            The node containing the key if found, otherwise None.
        """
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def display_tree(self, node, level=0):
        """
        Displays the tree structure with indentation representing depth.

        Args:
            node: The current node to visit.
            level: The current level of depth (used for indentation).
        """
        if node is not None:
            self.display_tree(node.right, level + 1)
            print(" " * 4 * level + str(node.val))
            self.display_tree(node.left, level + 1)

# Example usage
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
        tree.display_tree(tree.root)
        print()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
