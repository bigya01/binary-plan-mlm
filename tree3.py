class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.list=[]
        self.signup_com=0
        self.sales=0
        self.balance_com=0
        self.total_com=0
        self.t_com=0

class BinaryTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self,val):
        if self.root is None:
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
                    node.signup_com+=20
                    node.t_com+=20

                elif side == 'r':
                    if node.right is not None :
                         print("items exist")
                    node.right = Node(val)
                    node.signup_com+=20
                    node.t_com+=20


                else:
                    # print("Invalid side.")
                     node.balance_com+=5
                     node.t_com+=5
    def sales(self):
         node_key=int(input("enter the node of which you want to add commision of"))
         node=self.search(self.root,node_key)
         sales=int(input("enter the sales of the node"))
         node.sales+=sales
         node.t_com+=sales

    def total_sales(self,node,key):
         if node.left is None and node.right is None:
              return node.total_com
         else:    
            if node.left.t_com>node.right.t_com:
                node.total_com+=node.tcom+ 0.5*node.right.sales
                return node.total_com
            else:
                node.total_com+=node.tcom+ 0.5*node.left.sales
                return node.total_com
    def search(self, node, key):
        if node is None or node.val == key:
            return node
        result=self.search(node.left,key)
        if result is not None:
             return result
        if node.val==key:
             return node
        return self.search(node.right,key)
    def preorder_traversal(self,root):
        if root is not None:
            list.append(root)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
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
        print("traversal")
        tree.preorder_traversal(tree.root)
    else:
        print("Invalid choice.")









