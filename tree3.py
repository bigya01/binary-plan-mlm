class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self,val,parent_key,side):
        if self.root is None:
            self.root = Node(val)
        else:
            # parent_key = int(input("Enter parent key: "))
            node = self.search(self.root, parent_key)
            if node is None:
                print("Parent key not found.")
            else:
                # side = input("Insert in left or right (l/r)? ").lower()
                # val = int(input("Enter value: "))
                if side == 'l':
                    if node.left is not None :
                        print ("items exist")
                    node.left = Node(val)
                elif side == 'r':
                    if node.right is not None :
                         print("items exist")
                    node.right = Node(val)
                else:
                    print("Invalid side.")

    def search(self, node, key):
        if node is None or node.val == key:
            return node
        result=self.search(node.left,key)
        if result is not None:
             return result
        if node.val==key:
             return node
        return self.search(node.right,key)
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
        tree.insert(val,parent_key,side)
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