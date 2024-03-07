class Tree:
    def __init__(self, data =None) -> None:
        self.left = None
        self.right = None
        self.data = data
    def search(self, root, data):
        if root.data == data or root is None:   
            return root
        left = self.search(root.left, data)
        
    def insert(side, parent, data):
        pass