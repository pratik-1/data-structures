class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def dfs_preorder(self):
        results = []

        def traverse(node):
            results.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return results

    def dfs_postorder(self):
        results = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            results.append(node.value)

        traverse(self.root)
        return results

    def dfs_inorder(self):
        results = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            results.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)
        return results


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(
    "Pre-order: ",
    my_tree.dfs_preorder(),
    "\nExpected: [47, 21, 18, 27, 76, 52, 82]",
)

print(
    "\nPost-order: ",
    my_tree.dfs_postorder(),
    "\nExpected: [18, 27, 21, 52, 82, 76, 47]",
)

print(
    "\nIn-order: ",
    my_tree.dfs_inorder(),
    "\nExpected: [18, 21, 27, 47, 52, 76, 82]",
)
