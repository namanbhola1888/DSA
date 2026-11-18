class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root



obj = BinarySearchTree()
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = obj.insert(root, value) 




'''
#	Problem	

1	Search in BST
2	Find Minimum 
3	Find Maximum 
4	Insert into BST
5	Delete Node 
6	Validate Binary

'''