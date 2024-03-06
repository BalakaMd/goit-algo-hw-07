# Двійкове дерево пошуку (Binary Search Tree) - Алгоритми пошуку

У цьому репозиторії містяться прості алгоритми для пошуку максимального, мінімального значень та суми всіх значень у
двійковому дереві пошуку.

## Приклади

### Завдання 1: Знаходження найбільшого значення в дереві

```python
def find_max_value(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.val


# Приклад використання:
max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)
```

### Завдання 2: Знаходження найменшого значення в дереві

```python
def find_min_value(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.val


# Приклад використання:
min_value = find_min_value(root)
print("Найменше значення в дереві:", min_value)
```

### Завдання 3: Знаходження суми всіх значень в дереві

```python
def tree_sum(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


# Приклад використання:
total_sum = tree_sum(root)
print("Сума всіх значень в дереві:", total_sum)
```
