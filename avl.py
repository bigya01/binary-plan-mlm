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
                self.balancing(node)
                # else:
                #     print("BOTH SIDES ARE ALREADY FILLED")
    
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
                    return self.right_rotate(node.left)
                node=self.left_rotate(node)
            elif balance_Factor<-1:
                if self.height(node.right)>0:
                    return self.left_rotate(node.right)
                node=self.right_rotate(node)
            else: 
                print("tree is balanced")
            self.balancing(node.left)
            self.balancing(node.right)
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





            