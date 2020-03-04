#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        i = None
        j = head
        while j:
            next_j = j.next
            j.next = i
            i = j
            j = next_j
        return i


def pl(head: ListNode):
    while head:
        print(head.val, end=" ")
        head = head.next
    print("")


if __name__ == "__main__":
    print("hi")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    print("Base list:")
    pl(a)
    print("Reversed list:")
    S = Solution()
    b = S.reverseList(a)
    pl(b)
