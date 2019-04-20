class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                # quedan menos de k nodos, se dejan como estan
                break
            group_next = kth.next

            # invertir el bloque; el primer nodo termina apuntando a group_next
            prev = group_next
            current = group_prev.next
            while current is not group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # kth es la nueva cabeza del bloque y el antiguo primero ahora es el ultimo
            old_first = group_prev.next
            group_prev.next = kth
            group_prev = old_first

        return dummy.next

    def get_kth(self, node: ListNode | None, k: int) -> ListNode | None:
        # avanza k nodos desde node; devuelve None si no alcanzan
        while node and k > 0:
            node = node.next
            k -= 1
        return node


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

    assert to_list(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(s.reverseKGroup(build_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(s.reverseKGroup(build_list([1, 2, 3]), 1)) == [1, 2, 3]
    assert to_list(s.reverseKGroup(build_list([1]), 1)) == [1]
    assert to_list(s.reverseKGroup(build_list([1, 2, 3, 4]), 4)) == [4, 3, 2, 1]
    assert to_list(s.reverseKGroup(build_list([1, 2, 3, 4, 5, 6]), 3)) == [3, 2, 1, 6, 5, 4]

    print("ok")
