import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        # (valor, indice de la lista, nodo); el indice desempata para no comparar nodos
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def build_lists(groups):
    return [build_list(values) for values in groups]


if __name__ == "__main__":
    s = Solution()

    assert to_list(s.mergeKLists(build_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(s.mergeKLists(build_lists([]))) == []
    assert to_list(s.mergeKLists(build_lists([[]]))) == []
    assert to_list(s.mergeKLists(build_lists([[1], [0]]))) == [0, 1]
    assert to_list(s.mergeKLists(build_lists([[], [2, 2], [1, 2, 3]]))) == [1, 2, 2, 2, 3]
    assert to_list(s.mergeKLists(build_lists([[-1, 5]]))) == [-1, 5]

    print("ok")
