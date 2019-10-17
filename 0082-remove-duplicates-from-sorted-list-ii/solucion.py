class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # nodo ficticio por si hay que borrar desde la cabeza
        dummy = ListNode(0, head)
        prev = dummy  # ultimo nodo que seguro se queda
        current = head

        while current:
            if current.next and current.next.val == current.val:
                # se salta todo el bloque con este valor
                value = current.val
                while current and current.val == value:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

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

    assert to_list(s.deleteDuplicates(build_list([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
    assert to_list(s.deleteDuplicates(build_list([1, 1, 1, 2, 3]))) == [2, 3]
    assert to_list(s.deleteDuplicates(build_list([]))) == []
    assert to_list(s.deleteDuplicates(build_list([1, 1]))) == []
    assert to_list(s.deleteDuplicates(build_list([1, 2, 2]))) == [1]
    assert to_list(s.deleteDuplicates(build_list([-3, -3, 0, 1, 1]))) == [0]

    print("ok")
