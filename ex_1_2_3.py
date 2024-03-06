class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


# Завдання 1: Знаходження найбільшого значення в дереві
def find_max_value(root):
    if root is None:
        return None
    current = root
    while current.right:
        current = current.right
    return current.val


# Завдання 2: Знаходження найменшого значення в дереві
def find_min_value(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.val


# Завдання 3: Знаходження суми всіх значень в дереві

def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)

max_value = find_max_value(root)
min_value = find_min_value(root)
total_sum = tree_sum(root)

print("Найбільше значення в дереві:", max_value)
print("Сума всіх значень в дереві:", total_sum)
print("Найменше значення в дереві:", min_value)
