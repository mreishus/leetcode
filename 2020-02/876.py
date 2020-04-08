#!/usr/bin/env python

# Middle of the Linked List

# Given a non-empty, singly linked list with head node head, return a middle
# node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: [1,2,3,4,5] Output: Node 3 from this list (Serialization: [3,4,5]) The
# returned node has value 3.  (The judge's serialization of this node is
# [3,4,5]).  Note that we returned a ListNode object ans, such that: ans.val =
# 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Example 2:

# Input: [1,2,3,4,5,6] Output: Node 4 from this list (Serialization: [4,5,6])
# Since the list has two middle nodes with values 3 and 4, we return the second
# one.

# Idea: Use fast and slow pointers
# [1, 2, 3, 4, 5] example
# Slow 1 -> 2 -> 3
# Fast 1 -> 3 -> 5
# Fast no longer has a fast.next - return slow

# [1,2,3,4,5,6] example
# Slow 1 -> 2 -> 3
# Fast 1 -> 3 -> 5
# Fast has fast.next, but not fast.next.next
# return slow.next


# Note:
#     The number of nodes in the given list will be between 1 and 100.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            return slow.next
        return slow


if __name__ == "__main__":
    print("876")
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    middle = Solution().middleNode(l1)
    print("Expect: 2")
    print(middle.val)
    l1.next.next.next = ListNode(4)
    middle = Solution().middleNode(l1)
    print("Expect: 3")
    print(middle.val)
