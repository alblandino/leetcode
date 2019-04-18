class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # prev -> first -> second -> resto  pasa a  prev -> second -> first -> resto
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

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

    assert to_list(s.swapPairs(build_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert to_list(s.swapPairs(build_list([]))) == []
    assert to_list(s.swapPairs(build_list([1]))) == [1]
    assert to_list(s.swapPairs(build_list([1, 2, 3]))) == [2, 1, 3]
    assert to_list(s.swapPairs(build_list([1, 2, 3, 4, 5, 6]))) == [2, 1, 4, 3, 6, 5]

    # se mueven los nodos, no los valores: la nueva cabeza es el antiguo segundo nodo
    head = build_list([1, 2])
    second = head.next
    assert s.swapPairs(head) is second

    print("ok")
