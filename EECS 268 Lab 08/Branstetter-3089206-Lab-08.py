'''
Author: Clayton Branstetter
KUID: 3089206
Date: 04/19/2022
Lab: lab#08
Last modified: 04/24/2022
Purpose: BSTs Phase 1
'''

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
        # create new node
        if self is None:
            return tree(data_item=ndata_item)

        else:
            key, nkey = ndata_item.number, self.data_item.number
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
        if key < data_item.number:
            return self.right.search(key)

        if self.left:
            # Key is smaller than root's key
            return self.left.search(key)
        print("pokemon not found\n")
        return 0

    def inorder(self):
        #Traverse LST
        if self.right:
            self.right.inorder()

        #Visit
        print(self)

        #Traverse RST
        if self.left:
            self.left.inorder()

    def postorder(self):
        #Traverse LST
        if self.right:
            self.right.postorder()

        #Traverse RST
        if self.left:
            self.left.postorder()

        #Visit
        print(self)

    def preorder(self):
        #Visit
        print(self)

        #Traverse LST
        if self.right:
            self.right.preorder()

        #Traverse RST
        if self.left:
            self.left.preorder()

    def __str__(self):
        return f"{self.data_item.US_name}\t {self.data_item.number}\t {self.data_item.JP_name}"


def format(file_name):
    with open(file_name, "r") as f: #open the file
        lines = f.read().split('\n')

    i=0
    for line in lines:
        [US_name, number, JP_name] = line.split('\t')
        data_item = Data_item(US_name, int(number), JP_name)
        if i==0:
            Tree = tree(data_item) #create a tree
            i+=1
        else:
            Tree.insert(data_item) #add all data items
    return Tree

def menu():
    print("\n1- Search\n2- Add\n3- Print\n4- Quit\n")
    n = input(" Choose an option : ")
    if n.isdigit() and (n in ["1","2","3","4"]):
        return int(n)
    print(" invalid input\n")
    return menu()

def main():
    file_name = input(" Enter the file name : ")
    Pokedex = format(file_name)
    n = menu()
    while n:
        if n == 1:
            key = input(" Enter a pokedex id : ")
            if key.isdigit():
                Pokedex.search(int(key))

        elif n == 2:
            US_name = input(" Enter the us name : ")
            number = input(" Enter the pokedex id : ")
            JP_name = input(" Enter the jp name : ")
            if number.isdigit():
                data_item = Data_item(US_name, number, JP_name)
                try:
                    Pokedex.insert(data_item)
                except:
                    print(" pokemon already exist\n")

        elif n == 3:
            order = input(" Enter the Traversal order, in, pre, or post order (in,pre,post): ").lower().strip()
            if order == 'in':
                Pokedex.inorder()
            elif order == 'pre':
                Pokedex.preorder()
            elif order == 'post':
                Pokedex.postorder()
            else:
                print('invalid input')

        else:return 0

        n = menu()

main()
