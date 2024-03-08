class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.val)


class AVLTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def insert(self, val):
        self.root = self.insert_(self.root, val)

    def delete(self, val):
        self.root = self.delete_(self.root, val)

    def insert_(self, node, val):
        if node is None:
            return Node(val)
            # self.root = Node(val)
            # node.val=val
        elif val < node.val:
            # if node.left is None:
            #     # If left child is None, create a new node
            #     node.left = Node(val)
            # else:
            node.left = self.insert_(node.left, val)
        else:
            # if node.right is None:
            #     # If left child is None, create a new node
            #     node.right = Node(val)
            # else:
            node.right = self.insert_(node.right, val)
        return self.balancing(node)

    def search(self, node, val):
        if node is None or node.val == val:
            return node
        else:
            if val < node.val:
                return self.search(node.left, val)
            else:
                return self.search(node.right, val)

    def height(self, node):
        if node is None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight+1
            else:
                return rheight+1

    def bf(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left)-self.height(node.right)

    def update_height(self, node):
        return max(self.height(node.left), self.height(node.right))+1

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        y.left = node
        self.update_height(node)
        self.update_height(y)
        return y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        y.right = node
        self.update_height(node)
        self.update_height(y)
        return y

        # def left_right(self,node):
        #     node.left=left_rotate(node.left)
        #     return right_rotate(node)

        # def right_left(self,node):
        #     node.right=right_rotate(node.right)
        #     return left_rotate(node)

    def balancing(self, node):
        balance_Factor = self.bf(node)
        if balance_Factor > 1:
            if self.height(node.left.right) > self.height(node.left.left):
                # if self.bf(node.left)<0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        elif balance_Factor < -1:
            # if self.bf(node.right)>0:
            if self.height(node.right.left) > self.height(node.right.right):
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def generate_DOT(self):
        def generate_DOT_r(node):
            nonlocal res
            if node is None:
                return
            if node is not None:
                res += f"{node.val} [color= \"{'red' if node == self.root else 'blue'}\"];\n"
            if node.left is not None:
                res += f"{node.val} -> {node.left.val};\n"
            if node.right is not None:
                res += f"{node.val} -> {node.right.val};\n"
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

    def get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete_(self, node, val):
        if not node:
            return node
        elif val < node.val:
            node.left = self.delete_(node.left, val)
        elif val > node.val:
            node.right = self.delete_(node.right, val)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.get_min_value_node(node.right)
            node.val = temp.val
            node.right = self.delete_(node.right, temp.val)
        if node is None:
            return node

        return self.balancing(node)


if __name__ == "__main__":
    tree = AVLTree()
    tree.root = tree.insert(tree.root, 8)
    tree.root = tree.insert(tree.root, 4)
    tree.root = tree.insert(tree.root, 3)
    print(tree.generate_DOT())
