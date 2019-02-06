class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        carry = 0

        # se sigue mientras quede algun digito o un acarreo pendiente
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next

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

    assert to_list(s.addTwoNumbers(build_list([2, 4, 3]), build_list([5, 6, 4]))) == [7, 0, 8]
    assert to_list(s.addTwoNumbers(build_list([0]), build_list([0]))) == [0]
    assert to_list(
        s.addTwoNumbers(build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9]))
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    assert to_list(s.addTwoNumbers(build_list([5]), build_list([5]))) == [0, 1]
    assert to_list(s.addTwoNumbers(build_list([1, 8]), build_list([0]))) == [1, 8]
    assert to_list(s.addTwoNumbers(build_list([9]), build_list([1, 9, 9]))) == [0, 0, 0, 1]

    print("ok")
