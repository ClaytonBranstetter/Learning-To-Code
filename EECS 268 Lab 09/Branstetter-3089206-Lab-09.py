from Tree import *

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
    print("\n1- Search\n2- Add\n3- Print\n4- Remove\n5- Copy\n6- Quit")
    options = ["1","2","3","4","5","6"]
    n = input("Choose an option : ")
    if n.isdigit() and (n in options):
        return int(n)
    print("invalid input\n")
    return menu()

    
def main():
    file_name = input("Enter the file name : ")
    main_pokedex = format(file_name)
    Pokedex = main_pokedex
    copy_pokedex = None
    copy = False
    n = menu()
    while n:
        if copy and (n not in [5,6]):
            p = input("Which pokedex are you interacting with ?\n1- Main Pokedex\n2- Copy Pokedex\n ")
            if int(p) == 1:
                Pokedex = main_pokedex
            else:
                Pokedex = copy_pokedex
        if n == 1:
            key = input("Enter a pokedex id : ")
            if key.isdigit():
                Pokedex.search(int(key))

        elif n == 2:
            US_name = input("Enter the us name : ")
            number = input("Enter the pokedex id : ")
            JP_name = input("Enter the jp name : ")
            if number.isdigit():
                data_item = Data_item(US_name, number, JP_name)
                try:
                    Pokedex.insert(data_item)
                except:
                    print("pokemon already exist\n")

        elif n == 3:
            order = input("Enter the Traversal order, in, pre, or post order (in,pre,post): ").lower().strip()
            if order == 'in':
                Pokedex.inorder(print)
            elif order == 'pre':
                Pokedex.preorder(print)
            elif order == 'post':
                Pokedex.postorder(print)
            else:
                print('invalid input')
        
        elif n == 4:
            key = input("Enter the id of the pokedex to remove : ")
            if key.isdigit():
                Pokedex.remove(int(key))

        elif n == 5:
            if copy:
                print("A copy already exist\n")
            else:
                copy_pokedex = main_pokedex.copy()
                copy = True
                print("\nPokedex is successfully copied\n")
        else:return 0
        
        n = menu()

main()