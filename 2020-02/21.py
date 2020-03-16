#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        pointer = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
                pointer = pointer.next
            else:  # l1.val >= l2.val:
                pointer.next = l2
                l2 = l2.next
                pointer = pointer.next
        while l1:
            pointer.next = l1
            l1 = l1.next
            pointer = pointer.next
        while l2:
            pointer.next = l2
            l2 = l2.next
            pointer = pointer.next
        return dummy_head.next


def pl(l1):
    if l1 is None:
        return
    pointer = l1
    while pointer:
        print(pointer.val, end=" ")
        pointer = pointer.next
    return pointer


if __name__ == "__main__":
    L1 = ListNode(1)
    L1.next = ListNode(2)
    L1.next.next = ListNode(4)
    L2 = ListNode(1)
    L2.next = ListNode(3)
    L2.next.next = ListNode(4)
    L3 = Solution().mergeTwoLists(L1, L2)
    pl(L3)
