class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # lo que sobre de una de las listas ya esta ordenado
        if list1:
            tail.next = list1
        else:
            tail.next = list2

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

    assert to_list(s.mergeTwoLists(build_list([1, 2, 4]), build_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(s.mergeTwoLists(build_list([]), build_list([]))) == []
    assert to_list(s.mergeTwoLists(build_list([]), build_list([0]))) == [0]
    assert to_list(s.mergeTwoLists(build_list([5]), build_list([1, 2, 3]))) == [1, 2, 3, 5]
    assert to_list(s.mergeTwoLists(build_list([-3, 0]), build_list([-2, -1, 4]))) == [-3, -2, -1, 0, 4]

    print("ok")
