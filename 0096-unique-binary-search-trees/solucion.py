class Solution:
    def numTrees(self, n: int) -> int:
        # count[i] = cantidad de BST distintos con i nodos
        count = [0] * (n + 1)
        count[0] = 1

        for nodes in range(1, n + 1):
            # cada valor como raiz: root - 1 nodos a la izquierda y el resto a la derecha
            for root in range(1, nodes + 1):
                count[nodes] += count[root - 1] * count[nodes - root]

        return count[n]


if __name__ == "__main__":
    s = Solution()

    assert s.numTrees(3) == 5
    assert s.numTrees(1) == 1
    assert s.numTrees(2) == 2
    assert s.numTrees(4) == 14
    assert s.numTrees(19) == 1767263190

    print("ok")
