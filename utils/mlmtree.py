class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.val


class BinaryMLMTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert_root(self, val):
        self.root = Node(val)

    def insert(self, val, parent_key, side):
        node = self.search(parent_key)
        if node is None:
            print("Parent key not found.")
        else:
            if side == 'Left':
                if node.left is not None:
                    print("items exist")
                node.left = Node(val)
            elif side == 'Right':
                if node.right is not None:
                    print("items exist")
                node.right = Node(val)
            else:
                print("Invalid side.")

    def search(self, key):
        def dfs_search(node, key):
            if node is None or node.val == key:
                return node
            # left search
            left_result = dfs_search(node.left, key)
            if left_result:
                return left_result
            # right search
            right_result = dfs_search(node.right, key)
            if right_result:
                return right_result

            return None

        return dfs_search(self.root, key)

    def get_nodes(self):
        def get_nodes_r(node):
            if node is None:
                return
            res.append(node)
            get_nodes_r(node.left)
            get_nodes_r(node.right)
        res = []
        get_nodes_r(self.root)
        return res

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

    def generate_DOT(self):
        def generate_DOT_r(node):
            nonlocal res
            if node is None:
                return
            if node.left is not None:
                res += f"{node.val} -> {node.left.val};\n"
            if node.right is not None:
                res += f"{node.val} -> {node.right.val};\n"
            if node.left is None and node.right is None:
                res += f"{node.val};\n"
            generate_DOT_r(node.left)
            generate_DOT_r(node.right)
        res = 'digraph mlm {\n'
        if self.root:
            res +=  f"{self.root.val} [color= \"Red\"];\n"
        generate_DOT_r(self.root)
        res += '}'
        return res


if __name__ == '__main__':
    tree = BinaryMLMTree()
    tree.insert_root('bindu')
    tree.insert('krishant','bindu', 'Left')
    tree.insert('krish', 'bindu', 'Right')
    tree.insert('k2', 'krishant', 'Left')
    tree.insert('k3', 'krish', 'Right')
    print(tree.generate_DOT())


#
