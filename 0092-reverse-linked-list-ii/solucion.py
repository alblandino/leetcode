class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummy = ListNode(0, head)

        # before queda en el nodo justo antes de la posicion left
        before = dummy
        for _ in range(left - 1):
            before = before.next

        # se invierte el tramo [left, right] como una lista normal
        prev = None
        current = before.next
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # before.next era el primero del tramo y ahora es el ultimo
        before.next.next = current
        before.next = prev
        return dummy.next


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    s = Solution()

    assert to_list(s.reverseBetween(build_list([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_list(s.reverseBetween(build_list([5]), 1, 1)) == [5]
    assert to_list(s.reverseBetween(build_list([3, 5]), 1, 2)) == [5, 3]
    assert to_list(s.reverseBetween(build_list([1, 2, 3]), 1, 3)) == [3, 2, 1]
    assert to_list(s.reverseBetween(build_list([1, 2, 3, 4]), 3, 4)) == [1, 2, 4, 3]
    assert to_list(s.reverseBetween(build_list([1, 2, 3]), 2, 2)) == [1, 2, 3]

    print("ok")
