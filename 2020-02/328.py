#!/usr/bin/env python
"""
328. Odd Even Linked List
Medium

Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

The relative order inside both the even and odd groups should remain as it
was in the input.

The first node is considered odd, the second node even
and so on ...

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        1 -> 2 -> 3 -> 4 -> 5 -> NULL
        i    j

        i goes to odd. Its outward arrow gets set to none.
        j goes to even. Its outward arrow gets set to none.

        i moves along to j.next (if j exists)
        j will move along next loop.
        """
        odd_head = ListNode(None)
        odd = odd_head
        even_head = ListNode(None)
        even = even_head

        i = head
        while i:
            j = i.next
            i.next = None

            odd.next = i
            odd = odd.next

            even.next = j
            even = even.next

            i = None
            if j:
                i = j.next
                j.next = None

        odd.next = even_head.next
        return odd_head.next


def print_ll(a):
    while a:
        print(a.val, end=" -> ")
        a = a.next
    print("NULL")


if __name__ == "__main__":
    print("Hello")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a = Solution().oddEvenList(a)
    print_ll(a)
