class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

    def preorder_print(self, start, traversal):
        if start:
            print(f"This is traversal 1: {traversal}")
            traversal += (str(start.value) + "-")
            print(f"This is traversal 2: {traversal}")
            traversal = self.preorder_print(start.left, traversal)
            print(f"This is traversal 3: {traversal}")
            traversal = self.preorder_print(start.right, traversal)
            print(f"This is traversal 4: {traversal}")
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(8)

    #print(tree.print_tree("preorder"))
    #print(tree.print_tree("inorder"))
    print(tree.print_tree("postorder"))
