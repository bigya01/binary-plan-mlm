class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color="black"
class AVLTree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None
    def insert(self,node,val):
        if node is None:
            # return Node(val)
            self.root = Node(val)
            # node.val=val
        elif val<node.val:
            self.insert(node.left,val)
        else:
            self.insert(node.right,val)
        # self.balancing(node)
            
    
    def search(self,node,val):
            if node is None or node.val==val:
                return node
            else:
                if val<node.val:
                    return self.search(node.left,val)
                else:
                    return self.search(node.right,val)
    def height(self,node):
            if node is None:
                return 0
            else:
                lheight=self.height(node.left)
                rheight=self.height(node.right)
                if lheight>rheight:
                    return lheight+1
                else:
                    return rheight+1
    def bf(self,node):
            if node is None:
                return 0
            else:
                return self.height(node.left)-self.height(node.right)
        
    def update_height(self,node):
            return max(self.height(node.left)+self.height(node.right))+1
        
    def left_rotate(self,node):
            y=node.right
            node.right=y.left
            y.left=node
            self.update_height(node)
            self.update_height(y)
            return y

    def right_rotate(self,node):
            y=node.left
            node.left=y.right
            y.right=node
            self.update_height(node)
            self.update_height(y)
            return y
        
        # def left_right(self,node):
        #     node.left=left_rotate(node.left)
        #     return right_rotate(node)
        
        # def right_left(self,node):
        #     node.right=right_rotate(node.right)
        #     return left_rotate(node)
        
    def balancing(self,node):
            if node is None:
                return None
            balance_Factor=self.height(node.left)-self.height(node.right)
            if balance_Factor>1:
                if self.height(node.left)<0:
                    return self.left_rotate(node.left)
                node=self.right_rotate(node)
            elif balance_Factor<-1:
                if self.height(node.right)>0:
                    return self.right_rotate(node.right)
                node=self.left_rotate(node)
            else: 
                print("tree is balanced")
            self.balancing(node.left)
            self.balancing(node.right)
    
    def generate_DOT(self):
        def generate_DOT_r(node):
            nonlocal res
            if node is None:
                return
            if node is not None:
                res += f"{node.val} [color= \"{node.color}\"];\n"
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




    def findlargestnode(self,node):
         if node is None or node.right is None:
              return node
         else:
              return self.findlargestnode(node.right)
    def delete(self,node,val):
        if node is None:
              print("value not found")
        elif val<node.data:
            self.delete(node.left,val)
        elif val>node.data:
            self.delete(node.right,val)
        elif node.left and node.left:
            temp=self.findlargestnode(node.left)
            node.val=temp.val
            self.delete(node.left,temp.val)
        else:
            temp=node
            if node.left is None and node.right is None:
                node=None
            elif node.left is not None:
                node=node.left
            else:
                node=node.right
            del(temp)
            self.update_height (node)
            self.bf(node)
            self.balancing(node)


if __name__=="__main__":
    tree=AVLTree()
    tree.insert(tree.root,8)
    tree.insert(tree.root,4)
    tree.insert(tree.root,3)
    print(tree.generate_DOT())


    


            