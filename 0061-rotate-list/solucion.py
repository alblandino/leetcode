class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head

        # largo de la lista y ultimo nodo
        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # la nueva cola queda length - k - 1 pasos despues de la cabeza
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head


def build_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    s = Solution()

    assert to_list(s.rotateRight(build_list([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert to_list(s.rotateRight(build_list([0, 1, 2]), 4)) == [2, 0, 1]

    assert to_list(s.rotateRight(build_list([]), 3)) == []
    assert to_list(s.rotateRight(build_list([7]), 2 * 10**9)) == [7]
    assert to_list(s.rotateRight(build_list([1, 2, 3]), 3)) == [1, 2, 3]
    assert to_list(s.rotateRight(build_list([1, 2]), 0)) == [1, 2]

    print("ok")
