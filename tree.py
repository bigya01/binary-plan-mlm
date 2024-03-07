# class TreeNode:
#     def __init__(self, key):
#         self.key = key
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key, parent_key=None, side=None):
#         """Function to insert a value into the binary tree."""
#         # If the tree is empty, the inserted key becomes the root
#         if not self.root:
#             self.root = TreeNode(key)
#             return

#         # If parent_key and side are provided, find the appropriate node
#         if parent_key is not None and side is not None:
#             parent_node = self._search_recursive(self.root, parent_key)
#             if parent_node is None:
#                 print("Parent not found.")
#                 return
#             if side == "left":
#                 parent_node.left = TreeNode(key)
#             elif side == "right":
#                 parent_node.right = TreeNode(key)
#             else:
#                 print("Invalid side specified.")
#         else:
#             print("Please specify parent key and side.")

#     def search(self, key):
#         """Function to search for a value in the binary tree."""
#         return self._search_recursive(self.root, key)

#     def _search_recursive(self, node, key):
#         """Helper function for recursive search."""
#         if node is None or node.key == key:
#             return node
#         if key < node.key:
#             return self._search_recursive(node.left, key)
#         return self._search_recursive(node.right, key)

#     def display(self):
#         """Function to display the binary tree."""
#         self._display_recursive(self.root, 0)

#     def _display_recursive(self, node, level):
#         """Helper function for recursive display."""
#         if node is not None:
#             self._display_recursive(node.right, level + 1)
#             print("   " * level + "->", node.key)
#             self._display_recursive(node.left, level + 1)

# # Example usage:
# if __name__ == "__main__":
#     tree = BinaryTree()

#     # Inserting values
#     tree.insert(5)  # Inserts as root
#     tree.insert(3, 5, "left")  # Inserts 3 as left child of 5
#     tree.insert(7, 5, "right")  # Inserts 7 as right child of 5
#     tree.insert(1, 3, "left")  # Inserts 1 as left child of 3
#     tree.insert(4, 3, "right")  # Inserts 4 as right child of 3
#     tree.insert(6, 7, "left")  # Inserts 6 as left child of 7
#     tree.insert(8, 7, "right")  # Inserts 8 as right child of 7

#     # Displaying the tree
#     print("Binary Tree:")
#     tree.display()

#     # Searching for a value
#     key_to_search = int(input("Enter the value to search: "))
#     found_node = tree.search(key_to_search)
#     if found_node:
#         print(f"Value {key_to_search} found in the tree.")
#     else:
#         print(f"Value {key_to_search} not found in the tree.")
