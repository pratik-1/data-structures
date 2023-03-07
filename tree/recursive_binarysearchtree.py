def _display_aux(node):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if node.right == None and node.left == None:
        line = "%s" % node.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right == None:
        lines, n, p, x = _display_aux(node.left)
        s = "%s" % node.value
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return (
            [first_line, second_line] + shifted_lines,
            n + u,
            p + 2,
            n + u // 2,
        )

    # Only right child.
    if node.left == None:
        lines, n, p, x = _display_aux(node.right)
        s = "%s" % node.value
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return (
            [first_line, second_line] + shifted_lines,
            n + u,
            p + 2,
            u // 2,
        )

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = "%s" % node.value
    u = len(s)
    first_line = (
        (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    )
    second_line = (
        x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    )
    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [
        a + u * " " + b for a, b in zipped_lines
    ]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def __rcontains(self, current_node, value):
        """
        if root == None return False
        if value == root return True
        if value < node call-contains(node.left, value)
        if value > node call-contains(node.right, value)
        """
        if current_node == None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self.__rcontains(current_node.left, value)
        else:
            return self.__rcontains(current_node.right, value)

    def rcontains(self, value):
        return self.__rcontains(self.root, value)

    def __rinsert(self, current_node, value):
        if current_node == None:
            return Node(value)
        elif value < current_node.value:
            current_node.left = self.__rinsert(current_node.left, value)
        else:
            current_node.right = self.__rinsert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__rinsert(self.root, value)

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value

    def __delete(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete(self, value):
        self.__delete(self.root, value)

    def display(self):
        lines, *_ = _display_aux(self.root)
        for line in lines:
            print(line)


my_tree = BinarySearchTree()
my_tree.r_insert(47)
my_tree.r_insert(21)
my_tree.r_insert(76)
my_tree.r_insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.r_insert(82)

print("BST Contains 27:")
print(my_tree.rcontains(27))

print("\nBST Contains 17:")
print(my_tree.rcontains(17))

print("\nBST before deleting 27:")
my_tree.display()
my_tree.delete(21)
print("\nBST after deleting 27:")
my_tree.display()
