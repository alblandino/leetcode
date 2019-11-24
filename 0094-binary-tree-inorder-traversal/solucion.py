from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        stack = []
        current = root

        while current or stack:
            # bajar por la izquierda todo lo posible
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result


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

    assert s.inorderTraversal(build_tree([1, None, 2, 3])) == [1, 3, 2]
    assert s.inorderTraversal(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])) == [
        4, 2, 6, 5, 7, 1, 3, 9, 8
    ]
    assert s.inorderTraversal(build_tree([])) == []
    assert s.inorderTraversal(build_tree([1])) == [1]
    assert s.inorderTraversal(build_tree([2, 1, 3])) == [1, 2, 3]
    assert s.inorderTraversal(build_tree([3, 2, None, 1])) == [1, 2, 3]
    assert s.inorderTraversal(build_tree([-1, None, -2, None, -3])) == [-1, -2, -3]

    print("ok")
