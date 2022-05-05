


class Data_item:
    def __init__(self, US_name, number, JP_name):
        self.number = number
        self.US_name = US_name
        self.JP_name = JP_name

class tree:
    def __init__(self, data_item):
        self.data_item = data_item
        self.right = None
        self.left = None

    def insert(self, ndata_item):
        #create new node
        if self is None:
            return tree(data_item=ndata_item)

        else:
            nkey, key = ndata_item.number, self.data_item.number
            # New key is equal than root's key
            if key == nkey:
                raise RuntimeError

            # New key is greater than root's key
            elif key < nkey:
                self.right = self.right.insert(ndata_item) if self.right else tree(data_item=ndata_item)

            # New key is smaller than root's key
            elif key > nkey:
                self.left = self.left.insert(ndata_item) if self.left else tree(data_item=ndata_item)

        return self

    def search(self, key):

        # Base Cases: root is null or key is present at root
        if self is None:
            return None

        data_item = self.data_item
        if data_item.number == key:
            print(self)
            return 1

        # Key is greater than root's key
        if key > data_item.number:
            return self.right.search(key)

        if self.left:
            # Key is smaller than root's key
            return self.left.search(key)
        print("pokemon not found\n")
        return 0

    def inorder(self,function):
        #Traverse LST
        if self.right:
            self.right.inorder(function)

        #Visit
        function(self)

        #Traverse RST
        if self.left:
            self.left.inorder(function)

    def postorder(self,function):
        #Traverse LST
        if self.left:
            self.left.postorder(function)

        #Traverse RST
        if self.right:
            self.right.postorder(function)

        #Visit
        function(self)

    def preorder(self,function):
        #Visit
        function(self)

        #Traverse LST
        if self.left:
            self.left.preorder(function)

        #Traverse RST
        if self.right:
            self.right.preorder(function)

    def __str__(self):
        return f"{self.data_item.US_name}\t {self.data_item.number}\t {self.data_item.JP_name}"

    # get the Node with the maximum key value and remove it
    def maxValueNode(self):
        parent = current = self
        i=0 #number of levels to reach the leaf node
        while(current.right):
            current = current.right
            i+=1

        for _ in range(i-1): #search for the parent of the leaf node
            parent = parent.right
        parent.right = None #delete the leaf left node
        return current.data_item #return the leaf left node

    def remove(self, key):
        if not self:
            return None

        tree_key = self.data_item.number
        if tree_key > key: #tree key > key look in the left subtree
            if self.left:
                self.left = self.left.remove(key)

        elif tree_key < key: #tree key < key look in the right subtree
            if self.right:
                self.right = self.right.remove(key)

        else: #key found
            if self.right == self.left == None: #the node if the leaf node of the tree
                return None #delete it

            elif self.right and self.left: #if the node has two children replace it with the leaf left node
                self.data_item = self.left.maxValueNode()

            else:
                self = self.right if self.right else self.left

        return self

    def copy(self):
        data = self.data_item
        new_data  = Data_item(data.US_name, data.number, data.JP_name)
        new_tree = tree(new_data) #create new tree
        #copy the right subtree
        if self.right:
            new_tree.right = self.right.copy()

        #copy the left subtree
        if self.left:
            new_tree.left = self.left.copy()
        return new_tree #return the new tree
