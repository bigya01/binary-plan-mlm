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

    def insert(self, val, parent_key):
        node = self.search(self.root, parent_key)
        def insert_node_with_spillover(node, val):
            if not node.left:
                node.left = Node(val)
            elif not node.right:
                node.right = Node(val)
            elif node.left and node.right:
                #recursion for spillover
                insert_node_with_spillover(node.left, val)
        insert_node_with_spillover(node, val)

    def search(self, node, key):
        if node is None or node.val == key:
            return node
        left_result=self.search(node.left,key)
        if left_result is not None:
             return left_result
        right_result=self.search(node.left,key)
        if right_result is not None:
             return right_result
        return None

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
    tree.insert('krishant','bindu')
    tree.insert('krish', 'bindu')
    tree.insert('k2', 'krishant')
    tree.insert('k3', 'krish')
    print(tree.generate_DOT())


#
