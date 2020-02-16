#!/usr/bin/env python

# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person and
# k is the number of people in front of this person who have a height greater
# than or equal to h. Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

from typing import List
from operator import itemgetter


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) == 0:
            return people
        people = sorted(people, key=itemgetter(1))
        people = sorted(people, key=itemgetter(0), reverse=True)
        # print("--")
        # print(people)
        # print("--")
        q = [people.pop(0)]
        for person in people:
            # print(f"Considering: {person}")
            # print(f"  Inserting at {person[1]}")
            q.insert(person[1], person)
            # print(q)
            # print("--")
        return q


s = Solution()
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
got = s.reconstructQueue(people)
want = [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
print(f"got {got} want {want} pass {got == want}")
