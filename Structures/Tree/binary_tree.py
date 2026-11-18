class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def createTree(self, arr, i=0):
        if i >= len(arr) or arr[i] is None:
            return None

        root = BinaryTree(arr[i])

        root.left = self.createTree(arr, 2*i+1)
        root.right = self.createTree(arr, 2*i+2)

        return root


    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)


    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")



arr = [10, 20, 30, 40, 50, 60, 70]

tree = BinaryTree(None)

root = tree.createTree(arr)

print("Inorder:")
tree.inorder(root)

print("\nPreorder:")
tree.preorder(root)

print("\nPostorder:")
tree.postorder(root)