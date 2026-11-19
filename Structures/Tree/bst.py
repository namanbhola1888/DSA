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


    def deleteNodeIterative(self, root, value):
        while root:
            if value == root.data:
                return True

            elif value < root.data:
                root = root.left

            else:
                root = root.right

        return False


    def deleteNodeRecusrive(self, root, value):
        if root is None:
            return

        if root.data == value:
            return True

        elif value < root.data:
            return self.deleteNodeRecusrive(root.left, value)

        else:
            return self.deleteNodeRecusrive(root.right, value)
        

    def findMinimumIterative(self, root):
        if root is None: 
            return

        while root.left:
            root = root.left

        return root.data
        

    def findMinimumRecursive(self, root):
        if root is None:
            return

        if root.left is None:
            return root.data

        return self.findMinimumRecursive(root.left)


    def findMaximumIterative(self, root):
        if root is None:
            return 

        while root.right:
            root = root.right

        return root.data


    def findMaximumRecursive(self, root):
        if root is None:
            return 

        if root.right is None:
            return root.data

        return self.findMaximumRecursive(root.right)
    



obj = BinarySearchTree()
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = obj.insert(root, value) 

minimum = obj.findMinimumIterative(root)
print(minimum)

minimum = obj.findMinimumRecursive(root)
print(minimum)

maximum = obj.findMaximumIterative(root)
print(maximum)

maximum = obj.findMaximumRecursive(root)
print(maximum)



'''
#	Problem	

1	Search in BST
2	Find Minimum 
3	Find Maximum 
4	Insert into BST
5	Delete Node 
6	Validate Binary

'''