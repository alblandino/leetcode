from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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

    assert s.isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    assert s.isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    assert s.isSameTree(build_tree([1, 2, 1]), build_tree([1, 1, 2])) is False
    assert s.isSameTree(build_tree([]), build_tree([])) is True
    assert s.isSameTree(build_tree([]), build_tree([1])) is False
    assert s.isSameTree(build_tree([1, 2]), build_tree([1, 2, 3])) is False
    assert s.isSameTree(build_tree([-5, None, 7]), build_tree([-5, None, 7])) is True

    print("ok")
