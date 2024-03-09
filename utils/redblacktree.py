class Node:
    def __init__(self, key, color="red"):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

    def __str__(self) -> str:
        return str(self.key)


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, "black")
        self.root = self.nil

    def insert(self, key):
        new_node = Node(key)
        current = self.root
        parent = None

        while current != self.nil:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = "red"

        self.fix_insert(new_node)

    def delete(self, key):
        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        def delete_node(z):
            y = z
            y_original_color = y.color
            if z.left == self.nil:
                x = z.right
                transplant(z, z.right)
            elif z.right == self.nil:
                x = z.left
                transplant(z, z.left)
            else:
                y = self.minimum(z.right)
                y_original_color = y.color
                x = y.right
                if y.parent == z:
                    x.parent = y
                else:
                    transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                transplant(z, y)
                y.left = z.left
                y.left.parent = y
                y.color = z.color
            if y_original_color == "black":
                self.fix_delete(x)

        node_to_delete = self.search(self.root, key)
        if node_to_delete != self.nil:
            delete_node(node_to_delete)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left

                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)

        self.root.color = "black"

    def fix_delete(self, node):
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.left_rotate(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.right_rotate(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.right_rotate(node.parent)
                    sibling = node.parent.left
                if sibling.right.color == "black" and sibling.left.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.left_rotate(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = "black"

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def search(self, node, key):
        while node != self.nil and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

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

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.nil:
            x.right.parent = y

        x.parent = y.parent

        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def inorder_traversal(self, node):
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(node.key, node.color)
            self.inorder_traversal(node.right)

    def generate_DOT(self):
        def generate_DOT_r(node):
            nonlocal res
            if node is self.nil:
                return
            if node is not self.nil and node is not self.root:
                res += f"{node.key} [color= \"{node.color}\"];\n"
            if node is self.root:
                res += f"{node.key} [color= \"{node.color}\", label=\"{node.key} (root)\"];\n"
            if node.left is not self.nil:
                res += f"{node.key} -> {node.left.key};\n"
            if node.right is not self.nil:
                res += f"{node.key} -> {node.right.key};\n"
            # if node.left is None and node.right is None:
            #     res += f"{node.val};\n"
            generate_DOT_r(node.left)
            generate_DOT_r(node.right)
        res = 'digraph mlm {\n'
        # if self.root:
        #     res +=  f"{self.root.val} [color= \"Red\"];\n"
        generate_DOT_r(self.root)
        res += '}'
        return res


# Example usage:
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    keys = [7, 3, 18, 10, 22, 8, 11, 26]
    for key in keys:
        rb_tree.insert(key)

    print(rb_tree.generate_DOT())
