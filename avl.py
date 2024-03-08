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
    def insert(self,node,val):
        if self.root is None:
            self.root = Node(val)
        else:
            # parent_key = int(input("Enter parent key: "))
                # side = input("Insert in left or right (l/r)? ").lower()
                # val = int(input("Enter value: "))
                if val<node.val:
                    # if self.root.left is not None :
                    #     print ("items exist")
                    self.insert(node.left,val)
                elif val>=node.val:
                    # if self.root.right is not None :
                    #      print("items exist")
                    self.insert(node.right,val)

                # else:
                #     print("BOTH SIDES ARE ALREADY FILLED")
    
        def search(self,node,val):
            if node is None or node.val==val:
                return node
            else:
                if val<node.val:
                    return search(node.left,val)
                else:
                    return search(node.right,val)
        def height(self,node):
            if node is None:
                return 0
            else:
                lheight=height(node.left)
                rheight=height(node.right)
                if lheight>rheight:
                    return lheight+1
                else:
                    return rheight+1
        def bf(self,node):
            if node is None:
                return 0
            else:
                return height(node.left)-height(node.right)
        
        def update_height(self,node):
            return max(height(node.left)+height(node.right))+1
        
        def left_rotate(self,node):
            y=node.right
            node.right=y.left
            y.left=node
            update_height(node)
            update_height(y)
            return y
        

        def right_rotate(self,node):
            y=node.left
            node.left=y.right
            y.right=node
            update_height(node)
            update_height(y)
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
            balance_Factor=height(node)
            if balance_Factor>1:
                if height(node.left)<0:
                    return right_rotate(node.left)
                node=left_rotate(node)
            elif balance_Factor<-1:
                if height(node.right)>0:
                    return left_rotate(node.right)
                node=right_rotate(node)



            
            