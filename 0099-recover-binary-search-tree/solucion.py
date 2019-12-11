from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None  # primer nodo fuera de lugar
        second = None  # segundo nodo fuera de lugar
        prev = None
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            # en inorden cada valor deberia ser mayor que el anterior
            if prev is not None and prev.val > current.val:
                if first is None:
                    first = prev
                second = current
            prev = current
            current = current.right

        # se devuelven los dos valores a su lugar
        first.val, second.val = second.val, first.val


def build_tree(values: list) -> TreeNode | None:
    # arma el arbol desde una lista en orden por niveles, con None para huecos
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: TreeNode | None) -> list:
    # recorrido por niveles con None en los huecos, como lo muestra LeetCode
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    # se quitan los None del final
    while values and values[-1] is None:
        values.pop()
    return values


def inorder(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def recover(s: Solution, values: list) -> TreeNode | None:
    root = build_tree(values)
    assert s.recoverTree(root) is None
    # el arbol arreglado debe ser un BST: inorden estrictamente creciente
    result = inorder(root)
    assert result == sorted(result) and len(set(result)) == len(result)
    return root


if __name__ == "__main__":
    s = Solution()

    assert tree_to_list(recover(s, [1, 3, None, None, 2])) == [3, 1, None, None, 2]
    assert tree_to_list(recover(s, [3, 1, 4, None, None, 2])) == [2, 1, 4, None, None, 3]

    # dos nodos seguidos en inorden (raiz y su hijo izquierdo)
    assert tree_to_list(recover(s, [1, 2, 3])) == [2, 1, 3]
    # dos nodos lejos: 1 y 7 intercambiados en un arbol completo
    assert tree_to_list(recover(s, [4, 2, 6, 7, 3, 5, 1])) == [4, 2, 6, 1, 3, 5, 7]
    # solo dos nodos y valores extremos
    assert tree_to_list(recover(s, [-2147483648, 2147483647])) == [2147483647, -2147483648]

    print("ok")
