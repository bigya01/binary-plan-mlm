import utils.settings as s
# import settings as s


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.sales = 0
        self.initial_com = 0
        self.total_com = 0
        self.added_members = 0
        self.color = 'blue'
        self.is_Balanced = False

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
        self.root.color = 'Red'

    def update_commission(self, node):
        node.initial_com = 0
        if node.left and node.right:
            node.is_Balanced=True
            node.initial_com += s.BALANCE_COMMISSION
        node.initial_com += (node.sales*s.PRODUCT_SOLD_COMMISSION +
                             node.added_members*s.SIGNUP_COMMISION)

    def insert(self, val, parent_key):
        node = self.search(self.root, parent_key)
        if not node:
            print("Not found")
        node.added_members += 1
        node.initial_com += s.SIGNUP_COMMISION

        def insert_node_with_spillover(node, val):
            if not node.left:
                node.left = Node(val)
                self.update_commission(node)

            elif not node.right:
                node.right = Node(val)
                self.update_commission(node)

            elif node.left and node.right:
                # node.intial_com+=BALANCE_COMMISSION
                # recursion for spillover
                insert_node_with_spillover(node.left, val)
        insert_node_with_spillover(node, val)

    def update_sales(self, node_key, sales):
        #  node_key=int(input("enter the node of which you want to add commision of"))
        node = self.search(self.root, node_key)
        #  sales=int(input("enter the sales of the node"))
        node.sales = sales
        self.update_commission(node)
        # self.total_commision(node)

    def total_sales(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.sales
        else:
            return node.sales + self.total_sales(node.left) + self.total_sales(node.right)

    def total_commision(self, node):
        node.total_com = node.initial_com
        if node.left is None and node.right is None:
            return node.initial_com
        else:
            if self.total_sales(node.left) > self.total_sales(node.right):
                node.total_com += s.SALES_VOLULME_PER*self.total_sales(node.right)
            else:
                node.total_com += s.SALES_VOLULME_PER*self.total_sales(node.left)
            return node.total_com

    def search(self, node, key):
        if node is None or node.val == key:
            return node
        left_result = self.search(node.left, key)
        if left_result is not None:
            return left_result
        right_result = self.search(node.right, key)
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

    def get_nodes_dict(self):
        def get_nodes_r(node):
            if node is None:
                return
            tmp = dict()
            tmp['Name'] = node.val
            tmp['Sales'] = node.sales
            tmp['Members Added'] = node.added_members
            self.total_commision(node)
            tmp['Total Commission'] = node.total_com
            res.append(tmp)
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
            if node is not None:
                res += f"{node.val} [color= \"{node.color}\", label=\"{node.val} | ${self.total_commision(node)}\"];\n"
            if node.left is not None:
                res += f"{node.val} -> {node.left.val};\n"
            if node.right is not None:
                res += f"{node.val} -> {node.right.val};\n"
            if node.left is None and node.right is None:
                res += f"{node.val};\n"
            generate_DOT_r(node.left)
            generate_DOT_r(node.right)
        res = 'digraph mlm {\n'
        # if self.root:
        #     res +=  f"{self.root.val} [color= \"Red\"];\n"
        generate_DOT_r(self.root)
        res += '}'
        return res


if __name__ == '__main__':
    tree = BinaryMLMTree()
    tree.insert_root('bindu')
    tree.insert('krishant', 'bindu')
    tree.insert('krish', 'bindu')
    tree.insert('k2', 'krishant')
    tree.insert('k3', 'krish')
    print(tree.generate_DOT())


#
