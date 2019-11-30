from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode | None]:
        def build(low: int, high: int) -> list[TreeNode | None]:
            # rango vacio: la unica opcion es el arbol vacio
            if low > high:
                return [None]

            trees = []
            for root_val in range(low, high + 1):
                # a la izquierda van los menores y a la derecha los mayores
                left_trees = build(low, root_val - 1)
                right_trees = build(root_val + 1, high)
                for left in left_trees:
                    for right in right_trees:
                        trees.append(TreeNode(root_val, left, right))
            return trees

        return build(1, n)


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


if __name__ == "__main__":
    s = Solution()

    expected = [[1, None, 2, None, 3], [1, None, 3, 2], [2, 1, 3], [3, 1, None, None, 2], [3, 2, None, 1]]
    result = [tree_to_list(tree) for tree in s.generateTrees(3)]
    assert sorted(result, key=str) == sorted(expected, key=str)

    assert [tree_to_list(tree) for tree in s.generateTrees(1)] == [[1]]

    # con 4 valores hay 14 arboles, todos distintos y todos BST validos
    trees = s.generateTrees(4)
    shapes = [str(tree_to_list(tree)) for tree in trees]
    assert len(trees) == 14
    assert len(set(shapes)) == 14
    for tree in trees:
        assert inorder(tree) == [1, 2, 3, 4]

    assert len(s.generateTrees(8)) == 1430

    print("ok")
