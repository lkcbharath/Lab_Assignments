class TreeNode: 
    def __init__(self, val,parent=None): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
        self.parent = parent
    def __str__(self):
    	return str(self.val)
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree: 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
        temp = TreeNode(key)
        # Step 1 - Perform normal BST 
        if not root:
            return temp
        elif root.val < key:
            root.right = self.insert(root.right,key)
        else:
            root.left = self.insert(root.left,key)

        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root

    def delete(self, root, key): 
  
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root 
  
        elif key < root.val: 
            root.left = self.delete(root.left, key) 
  
        elif key > root.val: 
            root.right = self.delete(root.right, key) 
  
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.successor(root.right) 
            root.val = temp.val 
            root.right = self.delete(root.right, 
                                      temp.val) 
  
        # If the tree has only one node, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.getBalance(root.left) >= 0: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.getBalance(root.right) <= 0: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.getBalance(root.left) < 0: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.getBalance(root.right) > 0: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root  
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

    def inOrder(self, root): 
  
        if not root: 
            return
        self.inOrder(root.left) 
        print("{0} ".format(root.val), end="") 
        self.inOrder(root.right) 

    def search(self,root,key):
        if(root==None):
            # print("It does not exist")
            return None
        while root!=None:
            if(root.val<key):
                root=root.right
            elif(root.val>key):
                root=root.left
            elif(root.val==key):
                return root
        return None

    def maximum(self,root):
        while root.right is not None:
            root=root.right
        return root

    def minimum(self,root):
        while root.left is not None:
            root=root.left
        return root

    def successor(self,root,key):
        key=self.search(root,key)
        
        if key.right is not None:
            return self.minimum(key.right)
        else:
            y = key.parent
            # print(y)
            while y is not None and key==y.right:
                 key = y
                 y = y.parent
            return y
    
    def predecessor(self, root):
        key=self.search(root,key)
        if key.left is not None:
            return self.maximum(key.left)
        else:
            y = key.parent
            while y is not None and key==y.left:
                key = y
                y = y.parent
            return y


        

def main(): 
    myTree = AVL_Tree() 
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
    for num in nums: 
        root = myTree.insert(root, num) 
    # Preorder Traversal 
    print("Preorder Traversal after insertion -") 
    myTree.inOrder(root) 
    print() 
    # Delete 
    key = 10
    root = myTree.delete(root, key) 
    # Preorder Traversal 
    print("Preorder Traversal after deletion -") 
    myTree.inOrder(root)
    #key=11
    #print(myTree.search(root,key))
    #print(myTree.minimum(root).val)
    key=6
    print((myTree.successor(root,key)).val)
    

if __name__ == '__main__':
    main()