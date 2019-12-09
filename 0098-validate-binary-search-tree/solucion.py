from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        # en un BST valido el recorrido inorden sale estrictamente creciente
        stack = []
        current = root
        prev_val = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev_val is not None and current.val <= prev_val:
                return False
            prev_val = current.val
            current = current.right

        return True


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


if __name__ == "__main__":
    s = Solution()

    assert s.isValidBST(build_tree([2, 1, 3])) is True
    assert s.isValidBST(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert s.isValidBST(build_tree([1, 1])) is False
    assert s.isValidBST(build_tree([5, 4, 6, None, None, 3, 7])) is False
    assert s.isValidBST(build_tree([2147483647])) is True
    assert s.isValidBST(build_tree([-2147483648, None, 2147483647])) is True

    # una sola rama de 5000 nodos crecientes hacia la derecha
    chain = [1]
    for value in range(2, 5001):
        chain.append(None)
        chain.append(value)
    assert s.isValidBST(build_tree(chain)) is True

    print("ok")
