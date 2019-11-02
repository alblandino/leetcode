class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        # dos listas con nodo ficticio: menores que x y el resto
        less_dummy = ListNode()
        greater_dummy = ListNode()
        less_tail = less_dummy
        greater_tail = greater_dummy

        current = head
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = current.next

        # se corta el final para no dejar un ciclo con enlaces viejos
        greater_tail.next = None
        less_tail.next = greater_dummy.next
        return less_dummy.next


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

    assert to_list(s.partition(build_list([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
    assert to_list(s.partition(build_list([2, 1]), 2)) == [1, 2]
    assert to_list(s.partition(build_list([]), 0)) == []
    assert to_list(s.partition(build_list([3, 1, 2]), 4)) == [3, 1, 2]
    assert to_list(s.partition(build_list([5, 4, 3]), 1)) == [5, 4, 3]
    assert to_list(s.partition(build_list([1, 4, 3, 0, 2, 5, 2]), 3)) == [1, 0, 2, 2, 4, 3, 5]

    print("ok")
