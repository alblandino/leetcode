class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        current = head

        while current and current.next:
            if current.next.val == current.val:
                # se salta la copia repetida sin avanzar
                current.next = current.next.next
            else:
                current = current.next

        return head


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

    assert to_list(s.deleteDuplicates(build_list([1, 1, 2]))) == [1, 2]
    assert to_list(s.deleteDuplicates(build_list([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert to_list(s.deleteDuplicates(build_list([]))) == []
    assert to_list(s.deleteDuplicates(build_list([7, 7, 7, 7]))) == [7]
    assert to_list(s.deleteDuplicates(build_list([-5, -1, 0]))) == [-5, -1, 0]

    print("ok")
