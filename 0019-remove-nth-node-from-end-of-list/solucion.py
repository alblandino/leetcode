class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # el nodo ficticio permite borrar la cabeza sin un caso especial
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # fast queda n + 1 nodos adelante de slow
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        # slow esta justo antes del nodo a borrar
        slow.next = slow.next.next
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


if __name__ == "__main__":
    s = Solution()

    assert to_list(s.removeNthFromEnd(build_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(s.removeNthFromEnd(build_list([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(build_list([1, 2]), 1)) == [1]
    assert to_list(s.removeNthFromEnd(build_list([1, 2]), 2)) == [2]
    assert to_list(s.removeNthFromEnd(build_list([1, 2, 3]), 3)) == [2, 3]
    assert to_list(s.removeNthFromEnd(build_list([1, 2, 3]), 2)) == [1, 3]

    print("ok")
